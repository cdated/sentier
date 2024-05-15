python_sources(
    name="lib",
    dependencies=[],
    overrides={
        "manage.py": {
            "dependencies": ["sentier/service/gaba/settings.py:lib"],
            "run_goal_use_sandbox":False,
            "restartable": True,
        },
    },
)

pex_binary(
    name="manage",
    entry_point="manage.py",
    dependencies=[
        ":lib",
    ],
)

python_requirement(
    name="django",
    requirements=["Django==4.2.13"],
)
