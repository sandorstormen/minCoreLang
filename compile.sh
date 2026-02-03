#!/bin/bash
uv run maltoolbox compile src/main/mal/main.mal langspec.json
zip -r compiled.mar langspec.json
rm langspec.json