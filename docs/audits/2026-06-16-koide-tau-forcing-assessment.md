# Koide tau-forcing: assessment (is $Q=\tfrac23$ a QOU constraint or an import?)

> **Bean.** [`k9td`](../../.beans/k9td--koide-tau-forcing-derivation.md) (parent `qz9k`).
> **Discipline.** Corpus-grep done (greenfield); formalize-first; the critical-distance
> license applies (Koide is the textbook numerology cautionary case — read its claim
> adversarially). This audit reports a **falsification against a fit**, not a derivation.

## The claim under test

The Koide relation for the charged leptons,
$$
Q \;=\; \frac{m_e + m_\mu + m_\tau}{\bigl(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau}\bigr)^2} \;=\; \frac{2}{3},
$$
holds empirically to $\sim 10^{-5}$. "Tau forcing" = solve $Q=\tfrac23$ for $m_\tau$ given
$(m_e,m_\mu)$. The question for QOU is **not** whether the number works — it does — but
whether the framework **derives** $Q=\tfrac23$ from independent categorical structure, or
whether forcing $m_\tau$ from it is a disguised fourth calibration input (CAL-4).

## Tier A — fact (the number, stated honestly)

Forcing $Q=\tfrac23$ with PDG inputs $m_e=0.51099895$, $m_\mu=105.6583755$ MeV gives a
quadratic in $\sqrt{m_\tau}$ whose physical (larger) root is
$$
m_\tau^{\text{Koide}} \;\approx\; 1776.97\ \text{MeV},
\qquad m_\tau^{\text{PDG}} = 1776.86\ \text{MeV}
\quad\Rightarrow\quad \text{rel. err } \approx 6.2\times10^{-5}\ (62\ \text{ppm}).
$$
For contrast, QOU's **own** best structural attempt — the single-knot cohomological
extension $m_\tau/m_e \approx \mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$ — was **exhaustively
falsified** at $\mathbf{1.33\%}$ (best candidate $\mathrm{Vol}(8_1)/\hbar_q^3$), i.e.
$\sim 13{,}000\times$ experimental precision, over 108 single-knot + $\binom{25}{2}\times6$
product candidates
([`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md)).

**So Koide beats QOU's own structural prediction by ~200×.** That gap is exactly why the
relation is tempting and exactly why it must be classified before use.

## Tier B — assessment (does QOU derive $Q=\tfrac23$? No.)

A genuine QOU derivation of Koide would require three categorical ingredients, each fixed
**independently** of the lepton masses:

1. **A $\mathbb{Z}/3$ generation structure.** Koide's $Q=\tfrac23$ is the statement that
   $(\sqrt{m_e},\sqrt{m_\mu},\sqrt{m_\tau})$ sits at $45^\circ$ to the democratic
   $(1,1,1)$ axis, with the three roots an orbit $\sqrt{m_k}\propto 1+\sqrt2\cos(2\pi k/3+\delta)$,
   $\delta\approx 0.222$. This needs a cyclic 3-fold symmetry on the generations.
   **QOU has none.** The lepton sector is indexed by **braid words in increasing $H_n(q)$**
   — electron $K_{\mathfrak e}=\sigma_1^3\in H_2(q)$, muon $K_\mu=(\sigma_1\sigma_2^{-1})^2\in H_3(q)$,
   tau "analogously" (unpinned)
   ([`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md) L1–5).
   That is a tower of growing strand number, **not** a $\mathbb{Z}/3$ orbit; there is no
   cyclic group acting on $\{\mathfrak e,\mu,\tau\}$ to host the Koide phase $\delta$.

2. **A $\sqrt{m}$-democracy principle.** Koide is democratic in $\sqrt{m}$, not $m$. QOU's
   mass map is $\mathfrak m(K)=m_e\,|\mathrm{tr}_M(\mathcal B_K)|\,\rho_K$ — a **modulus** of a
   Markov trace, so $m\propto|\mathrm{tr}_M|$ and $\sqrt m\propto|\mathrm{tr}_M|^{1/2}$. There
   is no categorical object whose value is the $\sqrt m$ "amplitude" and which is democratic
   across generations. (The one place a $\sqrt{\;}$ enters — $q^{1/2}$ in the per-braid
   tower — is a fibre coordinate, unrelated to a mass amplitude.)

3. **The specific ratio $2/3$.** The framework does host scattered $2/3$'s (surface-term
   $A^{2/3}$, Descartes coefficients), but **none** attaches to lepton generations. A $2/3$
   from an unrelated construction is a coincidence-basin hit, not a derivation.

**None of the three is present.** Therefore $Q=\tfrac23$ is not produced by QOU structure;
solving it for $m_\tau$ **imports** an external relation. Under
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
that is a **CAL-4** — a hard audit failure — because $m_\tau$ would then rest on
$(m_e,m_\mu,\text{external }2/3)$ rather than on $(m_e,Q_\beta,m_\pi)$ alone.

### Correction to a tempting but wrong sub-claim

A "torus-knot $\mathrm{Vol}=0$ lepton-dictionary inconsistency" (electron/tau on torus knots
$T(2,3)/T(2,7)$, which are non-hyperbolic so $\mathrm{Vol}=0$, while muon is hyperbolic $4_1$)
looks like a clean internal contradiction. **It is not, and should not be cited as one.** The
canonical lepton conjecture uses the **per-braid $q$-volume**
$\mathrm{Vol}_q^{\text{tower}}(K_\ell)\in\mathbb Z[q^{1/2},q^{-1/2}]$ (a Laurent polynomial,
nonzero for torus braids), which tends to the hyperbolic volume **only** in the Kashaev
$q\to1$ limit; and the electron is the calibration **unit** ($\mathcal F_e(q_0)=1$), so its
hyperbolic volume never enters. The hyperbolic-$\mathrm{Vol}=0$ fact bites only the
**SUPERSEDED** scalar-$\rho_q$ Skein LO form, which the canonical tower already replaces. (Flagged
here so the next agent does not promote the overstated version.)

## Tier C — what would change the verdict (the honest open direction)

The productive path for $m_\tau$ is **not** Koide. It is **Path A** of the canonical lepton
tower: derive the lepton-sector dimensional factor $\xi_\ell(q)$ analytically from the
per-braid mass tower, with the constraints already recorded there — bar-symmetry ($P_{\text{avg}}$),
$\mathrm{Im}(q)$-robustness, Kashaev recovery, and $\mathcal F_e(q_0)=1$, $\mathcal F_\mu(q_0)=206.77$
([`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md) §"Conjectural form", §"Derivation paths").
If such a derived $\xi_\ell$ **independently** produced lepton roots satisfying $Q=\tfrac23$,
*that* would be a QOU derivation of Koide. Nothing on the corpus does so today, and the file's
own Path B ("fit a functional form for $\xi_\ell$ that matches CODATA for all 3 leptons") is
explicitly a fit, not a derivation.

## Verdict (tiered)

| Tier | Statement | Status |
|------|-----------|--------|
| A | Koide forces $m_\tau\approx1776.97$ MeV, 62 ppm from PDG; ~200× better than QOU's refuted 1.33% knot search | **fact** |
| B | QOU derives no $\mathbb{Z}/3$ democracy, no $\sqrt m$-amplitude, no $2/3$ for generations | **fitted / CAL-4 if imported** |
| C | The non-fitting route to $m_\tau$ is Path A ($\xi_\ell(q)$ derivation), independent of Koide | **open** |

**Bottom line.** "Koide tau-forcing" is a numerology **import**, not a categorical
derivation, and is **out of scope** for production under the three-calibration discipline.
Recording it as a fit closes bean `k9td` against acceptance criterion (b). The live open
problem $m_\tau$ remains the $\xi_\ell(q)$ derivation, tracked by the canonical lepton tower
conjecture — Koide is at most an *external consistency check* on a future derived $\xi_\ell$,
never an input.

## See also

- [`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md) — the exhaustive single-knot/product search (refuted at 1.33%)
- [`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md) — canonical conjecture + open $\xi_\ell(q)$ (Path A)
- [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) — the $H^0/H^1/H^2$ CAL map that a CAL-4 violates
- `computations/mdl_bit_count.py` — the corpus's only prior `koide` mention: a numerology MDL benchmark ("a lone elegant match stays 'intriguing' for decades")
