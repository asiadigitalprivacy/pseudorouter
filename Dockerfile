FROM ubuntu:14.10

# Tell debconf to run in non-interactive mode
ENV DEBIAN_FRONTEND noninteractive

RUN bash -c '\
grep -v ^deb-src /etc/apt/sources.list > /tmp/_ && cat /tmp/_ > /etc/apt/sources.list && rm /tmp/_ ;\
apt-get update ;\
\
apt-get install -y build-essential git rsync wget gawk python-dev subversion \
                   unzip libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev gettext ;\
\
apt-get clean'

RUN bash -c '\
mkdir -p /pr ;\
\
localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || true ;\
echo "Etc/UTC" > /etc/timezone ;\
'

ENV LANG=C LANGUAGE=C GDM_LANG=C

ENTRYPOINT exec bash -c '\
git clone https://github.com/asiadigitalprivacy/pseudorouter pr ;\
cd pr ;\
./scripts/feeds update -a ;\
git checkout .config ;\
./scripts/feeds install -a ;\
make defconfig ;\
exec bash -i'
