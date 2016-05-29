sip = {
    "udp": {
        "port": "5060"
    },
    "tcp": {
        "port": "5060"
    },
    "tls": {
        "port": "5061"
    },
    "users": "sipaccounts.sqlite",
    "rtp": {
        "enable": "yes",
        "bistream": "dump as bistream",
        "mode": ["bistream", "pcap"],
        "pcap": {
            "path": "var/dionaea/rtp/{personality}/%Y-%m-%d/",
            "filename": "%H:%M:%S_{remote_host}_{remote_port}_in.pcap"
        }
    },
    "personalities": {
        "default": {
            "domain": "my-domain",
            "name": "my server",
            "personality": "generic",
            "serve": ["192.168.1.2"],
            "default_sdp": "default",
            "handle": ["REGISTER", "INVITE", "BYE", "CANCEL", "ACK", "OPTIONS"]
        },

    },
    "actions": {
        "bank-redirect": {
            "do": "redirect",
            "params": {
            }
        },
        "play-hello": {
            "do": "play",
            "params": {
                "file": "var/dionaea/.../file.ext"
            }
        }
    }
}
