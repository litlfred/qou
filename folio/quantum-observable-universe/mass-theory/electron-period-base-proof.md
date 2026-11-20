The recurrence ([Symplectic prolongation (det B = 1) gives a one-parameter recurrence](#prop:sl2-prolongation-recurrence))
fixes $a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}$ for all $n$, with base data
$(a_D^{(0)}, a_D^{(1)})$. By
[The Seiberg–Witten differential is the jet decomposition of the Archimedean realisation](#prop:jet-sw-tau-decomposition) the $n=0$
period is the unprolonged Seiberg--Witten period, i.e. the electron period
$a_D^{(e)}$; the calibration $a_D^{(0)} = m_e$ sets the leptonic scale (CAL-1).
The base value is then $a_D^{(0)} = m_e$
([`QOU.Mass.electron_period_is_base`](#prop:electron-period-base), the structure
projection `base0`). Evaluating the recurrence at $n=0$,
$$
a_D^{(2)} = \tau\,a_D^{(1)} - a_D^{(0)} = \tau\,a_D^{(1)} - m_e,
$$
so $m_e$ enters the higher periods through the recurrence rather than as a
prefactor (`second_period_contains_me`, by `T.recurrence 0` and `base0`).
$\qquad\blacksquare$
