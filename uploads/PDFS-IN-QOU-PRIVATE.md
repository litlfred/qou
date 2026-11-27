# PDFs held in qou-private

Owner ruling 2026-11-25: third-party PDFs stay in the private repository `litlfred/qou-private`, at the same paths. These were removed from public qou on that date. Git history was not rewritten.

- `uploads/0105047v2.pdf`
- `uploads/0207158v1.pdf`
- `uploads/0208154v2.pdf`
- `uploads/3M.pdf`
- `uploads/Cairns1951_193.pdf`
- `uploads/Download (2).pdf`
- `uploads/S0002-9904-1960-10400-4.pdf`
- `uploads/S0002-9939-1951-0046635-9.pdf`
- `uploads/gtm-1999-02-016p.pdf`
- `uploads/hales3.pdf`
- `uploads/pltop.pdf`
- `uploads/rolfsen.pdf`
- `uploads/tverberg.pdf`
- `uploads/zeemanpl.pdf`

Library entries whose PDF is held there (their derived KG, sections and structure.json stay in qou). These pointers lived in each entry's `structure.json` as `source.private_location` until 2026-11-27; that key is not in the `pdf-structure/v1` schema, which is strict, so `check:l1-complete` refused the site build on it.

- `library/arxiv-2202.03067v4/2202.03067v4.pdf`
- `library/arxiv-math-0104104v3/0104104v3.pdf`
- `library/arxiv-math-0409565v2/0409565v2.pdf`
- `library/arxiv-math-0602138v1/0602138v1.pdf`
