DEV_PORTS = {"sentier.service.gaba": 8400}


def get_dev_port(service: str) -> int:
    try:
        return DEV_PORTS[service]
    except KeyError:
        raise ValueError(f"No dev port found for service {service}")
