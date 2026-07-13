---
name: build-pdf
roles: [collaborator, owner]
user_invocable: true
description: >
  Builds the PDF locally in the workspace (main monolithic PDF and split per-chapter PDFs).
allowed-tools: Bash AskUserQuestion run_command
---

# /build-pdf

This command builds the PDF locally to save GitHub CI minutes. It generates the monolithic PDF (`main.pdf`) and the split per-chapter PDFs.

## Behavior
1. Run the `build.ts` script to generate `main.tex` and the chapters:
   ```bash
   bun run ../folio-assistant/content/pipeline/build.ts \
     content/quantum-observable-universe/quantum-observable-universe.ts \
     --out-dir chapters/ \
     --generate-main \
     --main-out main.tex \
     --preamble latex/preamble.tex
   ```
2. Compile the PDF using `latexmk`. If `latexmk` is not available natively in the workspace, use the Docker builder image fallback (as specified in `docs-generation.md`):
   ```bash
   latexmk -pdf main.tex || docker run --rm --entrypoint "" -v $(pwd):/work -w /work ghcr.io/litlfred/qou-paper-builder:latest latexmk -pdf main.tex
   ```
3. Split the generated `main.pdf` into individual per-chapter PDFs:
   ```bash
   mkdir -p chapters-pdf/
   python3 ../folio-assistant/scripts/split-pdf-by-chapter.py \
     --input main.pdf \
     --output-dir chapters-pdf/
   ```
4. Confirm to the user that the PDFs have been generated in the workspace and provide the paths (`main.pdf` and `chapters-pdf/`).
