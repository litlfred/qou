**Proposition (the electron mass is the base period of the tower).**

The prolonged Seiberg--Witten periods satisfy the one-parameter recurrence
$a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}$
([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)). Its
$n=0$ term is the *unprolonged* period — the **electron period** $a_D^{(e)}$
([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition): "the $n=0$
term is the electron period"). Identifying $a_D^{(e)}$ with the leptonic scale
$m_e$ (CAL-1) makes the first calibration the **base of the tower**: every
period is generated from the triple $(m_e,\,a_D^{(1)},\,\tau)$, so $m_e$
propagates into *every* term through the recurrence — it is not an external
multiplicative prefactor bolted onto the geometry.

Concretely the $n=2$ period is $a_D^{(2)} = \tau\,a_D^{(1)} - m_e$: the electron
scale appears explicitly. This is the cohomological role of CAL-1 — the
**scale (normalisation) of the rank-2 $W$-Hodge plane**, the $h^0$ datum of the
archimedean realisation. The proposition's `lean.ref`,
[`QOU.Mass.electron_period_is_base`](#prop:electron-period-base), proves the
base identity; its companion `QOU.Mass.second_period_contains_me` (same Lean
file) proves the $n=2$ propagation — both sorry-free.
