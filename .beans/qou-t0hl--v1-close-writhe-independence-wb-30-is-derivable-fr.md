---
# qou-t0hl
title: 'V1: close writhe-independence — w(B_3)=0 is DERIVABLE from the gluon unit'
status: todo
type: task
priority: normal
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-08-10T18:23:24Z
---

The eightfold-way requirement 'second invariant INDEPENDENT of the writhe' is
NOT proved; the published p/n argument is a non-sequitur (Y=w^2/4 reproduces both
rows -- WritheIndependenceCriterion.lean). The correct criterion is: two states
with EQUAL writhe and DIFFERENT Y.

THE PREMISE IS NOW DERIVABLE, which is what was missing:
  gluon unit      sigma_0 sigma_1^-1   -> writhe = +1 -1 = 0
  Borromean baryon B_3 = (sigma_0 sigma_1^-1)^3 -> writhe = 3(+1-1) = 0
  vacuum / empty braid                  -> writhe = 0
So w(baryon) = w(vacuum) = 0 by DIRECT COMPUTATION from the braid word, not by
hypothesis. With Y(baryon)=+1 (nucleon_hypercharge_eq_one, merged) and
Y(vacuum)=0, equal_writhe_distinct_Y_forces_non_factoring closes it.
This replaces baryon_vacuum_separating's assumed hypotheses with derived facts.
