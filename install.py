import launch

if not launch.is_installed("openai"):
    launch.run_pip("install --upgrade openai", "Requirement of Prompt-Maker")
