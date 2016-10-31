import yaml


def get_deploy_stanza():
    """Produce a deploy.yaml a la http://y/cep319"""
    stanza = {}
    stanza["pipeline"] = [
        {"instancename": "itest", },
        {"instancename": "security-check", },
        {"instancename": "push-to-registry", },
        {"instancename": "performance-check", },
        {"instancename": "dev.everything", },
        {"instancename": "stage.everything", "trigger_next_step_manually": True, },
        {"instancename": "prod.canary", "trigger_next_step_manually": True, },
        {"instancename": "prod.non_canary", },
    ]
    return stanza


def _yamlize(contents):
    return yaml.safe_dump(contents, explicit_start=True, default_flow_style=False)


def main():
    print _yamlize(get_deploy_stanza())


if __name__ == "__main__":
    main()
