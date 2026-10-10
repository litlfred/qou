---
# qou-prar
title: Recalibrate latex-preflight — 33 issues, all false, both real aborts missed
status: completed
type: task
priority: normal
created_at: 2026-08-16T22:57:51Z
updated_at: 2026-08-16T22:58:25Z
---

Closed 2026-08-16 in folio-assistant#129.

**The gate reported 33 issues on the qou paper, all 33 false — while
missing BOTH fatal aborts** that actually killed the build (bare
`aligned` outside math mode; U+02E3 in a rendered title). A gate with
that profile trains agents to ignore it.

**29 x undefined-macro.** Every one a standard command whose package is
loaded, all compiling fine in a 0-error build: \itshape \tiny
\footnotesize \hskip \ignorespaces \trivlist \endtrivlist \topsep
\labelsep \lbrack \rbrack \renewenvironment \proofname \@plus
\@minus \@addpunct \@endpefalse (kernel); \newtheoremstyle
\theoremstyle \pushQED \popQED (amsthm); \arctan \coth \limsup
\varsigma \rightrightarrows (amsmath/amssymb); \coloneqq (mathtools);
\colorlet (xcolor); \setlist (enumitem). Seeded 379 -> 408.

**4 x unmapped-unicode = 1 regex bug + 3 verified-safe chars.**
`extractMappedUnicode` matched \newunicodechar WITHOUT the `u` flag, so
`[^\s{}]` matched a single UTF-16 code unit — an astral-plane mapping
like `\newunicodechar{U+1D519}{...}` captured HALF a surrogate pair and
never matched the char `nonAsciiUses` reports (that one iterates code
points). So EVERY non-BMP mapping was invisible and produced a permanent
false hit against a declared character. One `u` flag kills the class.
The remaining three (o-double-acute, up-arrow, s-caron) are declared by
LaTeX's own utf8.def and were each confirmed by compiling against the
real preamble. Seeded 33 -> 36.

**Calibration principle recorded:** "unmapped" is NOT "crashes" —
utf8.def already covers the up-arrow while nabla and U+02E3 genuinely
abort. Only a compile probe distinguishes them; only compile-verified
chars were seeded. Do NOT widen the seed by inspection.

Result: `LaTeX preflight: OK clean (472 macros, 35 files)`.
