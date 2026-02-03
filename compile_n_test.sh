./compile.sh
uv run python test_lang.py src/main/resources/org.mal-lang.minCoreLang-1.0.0.mar
uv run malsim src/main/resources/scenarios/apt29_scenario1.yml