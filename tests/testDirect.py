import unittest
from image_builder import *

build()


class TestDirect(unittest.TestCase):

    def setUp(self):
        os.stat(IMG)
        mount()

    def tearDown(self):
        umount()

    def test_firewallIsEnabled(self):
        os.stat(MPOINT+"/etc/config/firewall")
        self.assertEqual(0, os.system("ls -l %s" % MPOINT+"/etc/config/firewall"))

    def test_noDefaultOpenWrtAP(self):
        os.stat(MPOINT+"/lib/wifi/mac80211.sh")
        self.assertEqual(256, os.system("egrep -i -q '^[^#].*OpenWrt' %s" % MPOINT+"/lib/wifi/mac80211.sh"))

