FROM python:3.14-alpine3.23

# Setup base
RUN \
    apk add --no-cache \
        bash \
        git \
    \
    && pip3 install \
        --no-cache-dir \
        --prefer-binary \
        --find-links "https://wheels.home-assistant.io/musllinux/" \
        "repository-updater @ git+https://github.com/killer0071234/repository-updater@a4b652513fc4aee93700b1d2c727813fc9466df6"

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
