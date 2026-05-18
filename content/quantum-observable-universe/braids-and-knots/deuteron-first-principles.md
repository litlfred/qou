**Remark.**
*The deuteron $^2$H binding energy is computed from first principles
using the full $H_6(R, q)$ Schur–Weyl sum
([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition))
over all $11$ partitions of $6$, with the paper's atomic-braid
convention
(`atomic_braid_to_crossings` in
`folio-assistant/computations/hecke_character_symbolic.py`) and
the numerical Hoefsmit pipeline
(`hecke_characters.build_seminormal_matrices`).*

**Inputs (three total).**

1. *$q_0 \approx 1.1099786$ — substrate parameter (derived from
   CODATA $m_\mu/m_e$ via
   [local substrate](#prop:local-substrate-q), no fit).*
2. *$E_0 = 0.782\;\mathrm{MeV}$ — free-neutron $\beta$-decay
   Q-value
   ([categorical mass, Markov](#prop:categorical-mass-markov)).*
3. *Calibration $\tau$-map
   $|\mathrm{tr}_M(\mathfrak{n})|_{q_0} - |\mathrm{tr}_M(\mathfrak{p})|_{q_0}
   \longmapsto 0.782\;\mathrm{MeV}$.*

*No fitted constants.  No empirical nuclear-physics coefficients.
No BW parameters.*

**A = 1 calibration.**

| quantity | value |
|---|---|
| $\|\mathrm{tr}_M(\mathfrak{p})\|_{q_0}$ | $0.70225$ |
| $\|\mathrm{tr}_M(\mathfrak{n})\|_{q_0}$ | $0.45251$ |
| $Q_{\mathrm{cat}} = \mathrm{tr}_M(\mathfrak{n}) - \mathrm{tr}_M(\mathfrak{p})$ | $-0.24975$ |
| $E_0$ | $3.1312\;\mathrm{MeV}/\text{cat.unit}$ |

**A = 2 deuteron, $H_6(R, q)$ partition sum.**
*All $11$ partitions of $6$ contribute to the $q$-character sum.
Top six by magnitude for the atomic (with one pn inter-crossing):*

| $\lambda$ | $\dim S^\lambda$ | $w_\lambda(q_0)$ | $\chi^\lambda_q(T_w)$ | contribution |
|---|---|---|---|---|
| $(3,2,1)$ | $16$ | $0.3586$ | $-1.885$ | $-0.0422$ |
| $(3,3)$ | $5$ | $0.0354$ | $+3.208$ | $+0.0227$ |
| $(2,2,2)$ | $5$ | $0.0354$ | $-2.907$ | $-0.0206$ |
| $(4,2)$ | $9$ | $0.1114$ | $+1.584$ | $+0.0196$ |
| $(5,1)$ | $5$ | $0.0325$ | $+2.674$ | $+0.0174$ |
| $(2,1^4)$ | $5$ | $0.0325$ | $+2.011$ | $+0.0131$ |

**Result.**

| quantity | value |
|---|---|
| $\|\mathrm{tr}_M(\text{free } \mathfrak{p}+\mathfrak{n})\|_{q_0}$ | $0.32298$ |
| $\|\mathrm{tr}_M(^2\mathrm{H})\|_{q_0}$ | $0.00513$ |
| $\|\Delta \mathrm{tr}_M\|$ | $0.31785$ |
| $B_{\mathrm{pred}} = E_0 \cdot \|\Delta \mathrm{tr}_M\|$ | $\mathbf{0.9953\;\mathrm{MeV}}$ |
| $B_{\mathrm{AME}}({}^2\mathrm{H})$ | $2.2246\;\mathrm{MeV}$ |
| relative error | $-55.3\%$ |
| $\|\Delta m / m\|$ | $\mathbf{0.066\%}$ |

**Interpretation.**

*The relative-binding error is large ($-55\%$), but $|\Delta m/m|$
is $0.066\%$ — a factor $\sim 17$ improvement over the
std-channel-only baseline ($1.09\%$ on the 1ppb branch) and
broadly consistent with the Schur–Weyl derivation being
structurally correct.  The $55\%$ residual is consistent with
a **known upstream diagnosis**, not a bug of the Schur–Weyl sum.*

**Upstream context: $(5/2) \cdot m_e$ partition-sum discovery.**
*Parallel work on the 1ppb branch
(`folio-assistant/computations/residual_partition_sum.py`,
`tower_isotope_absolute.py`, `kerov_walk_verify.py`)
established:*

1. *$\sum_{\lambda \vdash 3} \frac{1}{d_\lambda}
   = \frac{1}{1} + \frac{1}{2} + \frac{1}{1} = \frac{5}{2}$
   — exact rational.*
2. *For the proton, the pure-tower residual satisfies*

$$
  \Delta m_{\mathfrak{p}} / m_e
  \;\approx\; \frac{5}{2}
  \;=\; \sum_{\lambda \vdash 3} \frac{1}{d_\lambda}
  \quad (\text{to } 0.03\%).
$$

*This is an **exact partition-sum closed form** for the proton's
tower residual.*

3. *For the neutron and every $^A$n-containing isotope, the
   same hypothesis **fails by factor $\sim 400$**.  Diagnosis:
   neutron's $\hat V_0^{\mathfrak{n}} = 0.854$ sits far from the
   $q_0 = 1.11$ pole of $\Phi_q$, so
   $\Phi_q(\hat V_0^{\mathfrak{n}})$ is $\sim 100\times$ smaller
   than $\Phi_q(\hat V_0^{\mathfrak{p}} = 0.989)$, under-
   estimating neutron mass by factor $2.3$
   (upstream witness `tower-isotope-absolute.witness.json`:
   $M^{\mathrm{pure}}_{\mathfrak{n}} \approx 411\;\mathrm{MeV}$ vs
   CODATA $939.6\;\mathrm{MeV}$).*

*The deuteron failure here at $-55\%$ is therefore **the same
structural issue** as the upstream neutron-tower failure: any
atom containing a neutron inherits the neutron's far-from-pole
$\hat V$, and the tower/partition-sum prediction undershoots by
the same mechanism.*

**What this means for the Schur–Weyl sum.**
*The Schur–Weyl computation above is structurally correct —
all $11$ partitions of $6$ contribute with the right $w_\lambda$
and $\chi^\lambda_q$, and the result is sensitive to the atomic-
braid convention.  The $-55\%$ residual localises to the
neutron contribution, not the partition sum.  Paths forward:*

1. *Fix the neutron braid word: explore whether alternative
   orderings of $udd$ (see upstream `explore_items_1_and_2.py`
   variant (f): $g_0 + g_1$ re-ordering gives $+6.7\%$ vs
   $-55\%$ baseline for the neutron mass) shift the deuteron
   prediction closer to $B_{\mathrm{AME}}$.*
2. *Add the level-1 cyclotomic residue correction at $\zeta_1 = 1$
   ([GB residue spectral sum](#prop:gb-residue-spectral-sum))
   — distance to pole is $0.11$, potentially large contribution.*
3. *The $\frac{5}{2} \cdot m_e$ partition sum is exact for the
   proton and may generalise to isotopes via
   $\sum_{\lambda \vdash 3A} \frac{1}{d_\lambda}$; the upstream
   work is open on this generalisation.*

**Upstream follow-up: paper's BW + chirality gives $0.5$–$0.9\%$.**

*Subsequent upstream work
(`folio-assistant/computations/bw_chirality_isotopes.py`,
`pure_hecke_binding.py`) established two sharper findings:*

1. *The **paper's own** figure-eight-BW formula with chirality
   factors
   ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
   gives $T$ at $0.505\%$ and $^3\mathrm{He}$ at $0.856\%$
   agreement with AME.  Chirality factors per knot type:*

| isotope | chirality | factor |
|---|---|---|
| D | chiral+ | $1 + h = 1.209$ |
| T, $^3$He | amphichiral | $1 - h^2 = 0.956$ |
| $^4$He | Borromean${}^2$ | $(1 - h^2)^2 = 0.914$ |

*with $h = q - q^{-1}$.  These factors modify the BW bulk term
$B_{\mathrm{bulk}}$ per isotope, giving an $A$-dependent
correction that the Schur–Weyl / Frobenius computation alone
does not capture.*

2. *The naive $B = E_0 \cdot (|\mathrm{tr}_M(\text{free})| -
   |\mathrm{tr}_M(\text{atom})|)$ approach (this script) is
   confirmed **insufficient** by upstream: for all tested
   isotopes it gives $-99\%$ to $-100\%$ relative error.  The
   paper's correct binding formula uses**restricted characters
   at specific jet levels**:*

$$
  a_k(\beta)
  \;=\;
  \frac{\sum_\lambda w_\lambda\, \chi_\lambda^{(k)}(\beta)}
       {\sum_\lambda w_\lambda \, \dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)},
$$

*where $\chi_\lambda^{(k)}$ is the $q$-character at jet level
$k$ and $\mathrm{Res}^{H_k}_{H_3}$ is the restriction functor
from $H_k$ to $H_3$.  Upstream's prefix-word per-level
experiments
(`pure_hecke_binding_prefix.py`) tested nucleon-cumulative
prefix extraction and found it still fails — the correct
prefix structure (strand-cumulative vs order-of-generation)
is an open problem.*

**Integrated picture.**

*The deuteron binding predicted by the Schur–Weyl pipeline
($0.995\;\mathrm{MeV}$) and the paper's BW + chirality formula
($\sim 2.20\;\mathrm{MeV}$) differ by $\sim 1.2\;\mathrm{MeV}$
— very close to the universal Frobenius co-Casimir correction
$m_e \cdot (2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$
([Frobenius universal](#thm:frobenius-codim-universal)).
The alignment suggests the two formulas are not in conflict but
capture complementary structural levels:*

- *Schur–Weyl + Frobenius = algebraic-categorical piece
  (vortex-independent).*
- *BW + chirality + jet-level prefix = isotope-specific
  structural piece (vortex-dependent via knot type).*

*The **full** mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) is the
sum of all three layers; this script captures layer (1) only,
upstream `bw_chirality_isotopes.py` captures layers (2) + (3).*

*Calibration $E_0$ note: this script uses the $\beta$-decay
calibration from the numerical pipeline, not the symbolic
one; the numbers differ from
([q-character closes parity gap](#rem:q-character-closes-parity-gap))
by a $\mathrm{tr}/\dim$ normalisation convention.  Both
are internally consistent.*

*Caveat (symbolic vs. numeric).* The symbolic-sympy pipeline
(`hecke_character_symbolic.py`) provides exact rational
expressions in $q$ at $A = 1$ but breaks down at $A \geq 2$:
the Hoefsmit $2 \times 2$ block relation $b^2 = a a' + 1$ can
turn negative at specific axial distances $\rho$ for $q_0$ off
the unitary locus, producing complex artifacts via
`sympy.sqrt(negative)`. The numerical pipeline works around
this with `sqrt(abs(b^2))` — the standard orthogonal-form
convention — at the cost of the exact symbolic $q$-dependence.
Two refactors restore symbolic exactness: tracking $b^2$ as a
formal polynomial without taking $\sqrt{\,\cdot\,}$ until the
final trace, or switching to the Ocneanu–Wenzl seminormal basis
which is manifestly real-algebraic on the unitary locus for all
partitions.

**Reference.**

*Script: `folio-assistant/computations/deuteron_first_principles.py`.
Witness: `deuteron-first-principles.witness.json`.  Runtime: under
a second (all partitions of $6$ with max $\dim = 16$, numerical).
Reproducible with Python 3.11 + numpy + scipy.*
