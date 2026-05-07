#!/bin/bash
if [ -f src/main/resources/org.mal-lang.minCoreLang-1.0.0.mar ]; then
  rm src/main/resources/org.mal-lang.minCoreLang-1.0.0.mar
fi
uv run maltoolbox compile src/main/mal/main.mal langspec.json
zip -r src/main/resources/org.mal-lang.minCoreLang-1.0.0.mar langspec.json
rm langspec.json