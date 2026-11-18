---
# qou-tvsp
title: 'Remark at cor:pbw: freeness is necessary — PBW fails for Lie algebras over a general commutative ring'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:29:19Z
updated_at: 2026-10-04T15:23:23Z
parent: qou-q4oa
---

Sharpness remark for `content/unital-groebner-bases/unital-groebner-bases-chapter/`,
to land after (or with) the hypothesis fix in the sibling bean.

Content: the "free as an R-module" hypothesis is not cosmetic. Over a general
commutative ring PBW fails -- Shirshov 1953 and Cartier 1958 give counterexamples,
and the standard family is Cohn's L_p = Lie_K(x1,x2,x3 | y3x3 = y2x2 + y1x1) over
K = k[y1,y2,y3]/(y_i^p), conjectured (Cohn 1963) not to embed into its universal
enveloping associative algebra and proved for p = 2, 3, 5 by Bokut-Chen-Chen,
J. Algebra 337 (2011) 82-102.

HONESTY CONSTRAINT: the triage read only the one-paragraph report in
[bokutchen2015pbw] section 3.7. Shirshov 1953, Cartier 1958, Cohn 1963 and
Bokut-Chen-Chen 2011 have NOT been read and none of them is in
content/schema/references.ts. Either phrase the remark as reported-by-survey with
bokutchen2015pbw as the collecting citation, or read the primaries first and cite
them directly. Do not cite the primaries on the strength of a survey paragraph.
