# Vector-2 residues closed: the BN12 S′ spectrum and the GK D₅ product on 4₁ (2026-07-24)

**Tier:** closes the two named open sub-items of
[`2026-07-18-vector2-double-pincer-a5-b4.md`](2026-07-18-vector2-double-pincer-a5-b4.md)
(the A5 "BN12 real-structure spectrum" residue and the B4 "D₅ 4₁ product"
residue). Audit-only; **scope-(a)**; comparison-only; **no fit; nothing
wired**. The magnitude scalar $m \in (0, 1/\sqrt5)$ is **not** selected here.
Probes + witnesses:
[`vector2_a5_sprime_residue_probe.py`](../../computations/probes/vector2_a5_sprime_residue_probe.py),
[`gk_d5_cyclic_dilog_4one_probe.py`](../../computations/probes/gk_d5_cyclic_dilog_4one_probe.py).

## Context

The parent pincer located the *same algebraic number* $\sqrt5$ on both sides
(the He⁴ $[1^4]$ exchange spectrum $\{\pm\sqrt5, \pm1\}$; the quadratic Gauss
sum $g_5 = \sqrt5$ behind GK Cor 1.2's $1/\sqrt N$; the $\Sigma(2,3,5)$
S-matrix normalization) but stopped at two walls: BN12's printed
anti-involution matrix $S'$ was not in the corpus, and the GK
cyclic-dilogarithm product $\prod D_5$ on the explicit $4_1$ data was not
evaluated. Both walls are now removed — the data were extracted from the
uploaded papers' rendered PDF pages and **property-verified exactly before
use** (anti-guessing rule) — and both comparisons are decided.

## A5 residue — the BN12 anti-involution spectrum (CLOSES, scope-(a))

Source: Braden–Northover, SIGMA 8 (2012) 065
(`library/sigma12-065/sigma12-065.pdf`), pp. 8, 13, 14. Extracted matrices: the
intersection form $C$ of the homology basis $\alpha_{1..8}$ (p. 13, "precisely
the matrix claimed by Riera and Rodríguez"), the real-structure
anti-involution $S'$ (p. 14), the canonical form
$S = \bigl[\begin{smallmatrix} I & I \\ 0 & -I\end{smallmatrix}\bigr]$ (one
nondividing real oval), the symplectic $T$ (p. 14), and the basis-change
matrix (4.2) (p. 8).

**Transcription gates (all exact, machine-checked):** $C^{\mathsf T} = -C$,
$\det C = 1$; $S'^2 = I$; $S' C S'^{\mathsf T} = -C$ (anti-symplectic w.r.t.
the intersection form); $B_{4.2}^{\mathsf T} C B_{4.2} = J$;
$T^{\mathsf T} J T = J$, $\det T = 1$; and — resolving BN12's compressed
statement "$S := TS'T^{-1}$" — the exact conjugation from the printed
$\alpha$-basis $S'$ is $U S' U^{-1} = S$ with $U = T\,B_{4.2}^{\mathsf T}$
(the (4.2) canonicalisation applies first). The order-5 rotation $A$
(constructed from the paper's stated basis structure
$\alpha_{2k+1} = R^k\alpha_1$, $\alpha_{2k+2} = R^k\alpha_2$ with
$1 + R + \dots + R^4 = 0$) satisfies $A^5 = I$,
$\mathrm{charpoly}(A) = \Phi_5(x)^2$, $ACA^{\mathsf T} = C$, and the dihedral
relation $S'AS' = A^{-1}$ — so $\{A^k S'\}_{k=0}^4$ is the natural 5-member
family of anti-involutions.

**The comparison (all charpolys exact over $\mathbb Q$):**

| Twisted object | charpoly | field of spectrum |
|---|---|---|
| $S'C$ (symmetric 8×8 twist) | $x^8+x^7-22x^6-9x^5+38x^4+4x^3-16x^2+x+1$, **irreducible** | degree-8 — no rational or quadratic eigenvalue at all |
| $C A^k S'$, $k=1..4$ | four further degree-8 polys, none divisible by $(x^2-5)$ | — |
| odd $A$-block (4-dim) | $(x^2-2x-1)(x^2+2x-1)$ | $\mathbb Q(\sqrt2)$ — **silver**-ratio units $\pm(1{+}\sqrt2), \pm(\sqrt2{-}1)$ |
| even $A$-block (4-dim) | $(x+1)(x^3-3x+1)$ | $\mathbb Q(\zeta_9)^+$ — $-1,\ 2\cos(2\pi k/9)$ |
| $S'$-fixed / anti-fixed restrictions | $x^2(x-2)(x+3)$, $x^2(x-1)(x+2)$ | rank-2 degenerate, integer |
| **target** ($[1^4]$ exchange) | $(x-1)(x+1)(x^2-5)$ | $\mathbb Q(\sqrt5)$ |

The two 4-dim $A$-stable blocks (both also $S'$-stable) are the
$\mathbb Q$-forms of the two 4-dim standard-representation blocks of
$H_1 \otimes \mathbb Q = 2\cdot\mathrm{std}$; their twisted spectra live in
$\mathbb Q(\sqrt2)$ and $\mathbb Q(\zeta_9)^+$ — **wrong number fields
entirely**.

**Basis-independent falsifier.** Eigenvalues of a bilinear form are only
congruence-covariant, and $\mathbb Q$-congruence preserves $\det$ mod squares:
$\det(S'C) = 1$ vs $\det(S_{\mathrm{exch}}) = 5$ are **distinct square
classes**, so *no basis presentation whatsoever* of the Bring involution-twisted
intersection form is $\mathbb Q$-congruent to the exchange form. (Signatures
agree — both 0 — so the discriminant class is the discriminating invariant.)

**Recorded-not-interpreted coincidence.** In the canonical frame the universal
twist $J\cdot S$ has charpoly $(x^2+x-1)^4$ — the **golden-ratio units**
$(-1\pm\sqrt5)/2$, each with multiplicity 4. This is where a $\sqrt5$ *does*
live on the real-structure side, but (i) it is universal for *any* genus-4
curve with a one-nondividing-oval real structure (topological type only, not
Bring-specific), (ii) $\{(-1\pm\sqrt5)/2\} \ne \{\pm\sqrt5, \pm1\}$, and
(iii) it is congruent to $S'C$ (det class 1), hence equally obstructed.

**Verdict (scope-(a)):** the natural involution-twisted forms, alone, do not
reproduce the exchange spectrum $\{\pm\sqrt5, \pm1\}$ — in any of the five
natural presentations, and provably in **no** presentation (discriminant-class
obstruction). **The Bring leg of Vector 2 closes.** No structural exclusion of
level-5 geometry from the $\Delta_\lambda$ wall is claimed (that would be
scope-(b), requiring a proved invariant about the wall itself).

## B4 residue — the GK D₅ product on the explicit 4₁ data (CLOSES, scope-(a))

Source: Garoufalidis–Kashaev, arXiv:1411.6062v2
(`library/arxiv-1411.6062v2/1411.6062v2.pdf`), equations (1), (9), (10), (4)/(7), Thm 1.1 (15),
Cor 1.2 (18), Cor 1.3, App A (75). The $4_1$ state integral is
$\mathcal I_{1,2}(\mathsf b) = \int \Phi_{\mathsf b}(x)^2 e^{-\pi i x^2}dx$
((A,B) = (1,2), §2.2); its gluing data $g(z) = -z(1-z)^{-2}$ gives
$z_\pm = e(\pm 1/6)$ with branches $\log z_+ = 2\pi i/6$,
$\log z_- = 10\pi i/6$. At $\mathsf b^2 = 1/5$ ($N=5$, $M=1$):
$\theta_+(z_+) = e^{i\pi/15} = \zeta_{30}$, $\theta_+(z_-) = e^{i\pi/3}$,
$q_+ = \zeta_5$ — every algebraic ingredient lives in
$\mathbb Q(\zeta_{30})$.

**Validation chain (probe assertions):** the $D_5$ functional equation as an
exact polynomial identity in $\mathbb Q(\zeta_5)[x]$; the $\zeta_5$-branch
invariance $G_5^+(\zeta_5\theta)^5 P(\theta)^2 = G_5^+(\theta)^5
P(\zeta_5\theta)^2$ (with $P := (/D_5)^5$; GK Remarks 1.4/1.5) exactly for
both $\theta$'s; the $N=1$ machinery reproducing Cor 1.3 exactly (algebraic
factors) and to 40 digits (Rogers branches $R(z_+) = -\pi^2/12 + iV/2$,
$V = \mathrm{Vol}(4_1) \approx 2.0298832$,
$R(z_-) = -5\pi^2/12 - iV/2$); and the **end-to-end gold check** — the
assembled Cor 1.2 evaluation equals the *direct* Faddeev state integral
(App A (75), tensor quadrature validated at $\mathsf b = 1$ against GK's
closed form (2) to $5\cdot10^{-9}$):

$$
\mathcal I_{1,2}(1/\sqrt5) \approx 0.0286196521 + 0.1346448862\,i
\qquad (|\Delta| \approx 1.9\cdot 10^{-9}).
$$

**Exact D₅ data (all four values REAL, minpolys over $\mathbb Q$):**

| Object | minimal polynomial | value |
|---|---|---|
| $(/D_5(\zeta_{30};\zeta_5))^5$ | $x^4-46x^3-94x^2+79x+1$ | $\approx -0.0124742071$ |
| $(/D_5(e^{i\pi/3};\zeta_5))^5$ | $x^4+29x^3-69x^2+29x+1$ | $\approx -0.0320117823$ |
| $G_5^+(\zeta_{30})$ | $x^4-60x^3+960x^2-5175x+6525$ | $\approx 1.7916726703$ |
| $G_5^+(e^{i\pi/3})$ | $x^4-60x^3+885x^2-4500x+6525$ | $\approx 2.4215347503$ |

All four are **degree 4** $= [\mathbb Q(\zeta_{30})^+ : \mathbb Q]$: each
generates the *full* real quartic cyclotomic field $\mathbb Q(\zeta_{30})^+$.
Each minpoly factors over $\mathbb Q(\sqrt5)$ into two quadratics
($\mathbb Q(\sqrt5)$ *is* the quadratic subfield), but **none of the values
lies in $\mathbb Q(\sqrt5)$** — the D₅ data are strictly beyond golden-ratio
combinations.

**The B4 answer.** The evaluation assembles as

$$
\mathcal I_{1,2}(1/\sqrt5) = \frac{1}{\sqrt5}\Bigl[\,c_+\,e^{-V/(10\pi)} +
c_-\,e^{+V/(10\pi)}\Bigr],\qquad
|c_\pm| = \frac{G_5^+(\theta_\pm)}{\sqrt3\,\bigl|/D_5(\theta_\pm)\bigr|^2},
$$

with $|c_+| \approx 5.9743802594$, $|c_-| \approx 5.5386782405$ (40 dps in the
witness; $|c_\pm|^{10} \in \mathbb Q(\zeta_{30})^+$ exactly). The icosahedral
$\Sigma(2,3,5)$ vacuum row $(2/\sqrt5)(\sin\frac{\pi}{5}, \sin\frac{2\pi}{5})
\approx (0.5257, 0.8507)$ does **not** appear: the exact in-field comparisons
$|c_\pm|^{10} = ((5\mp\sqrt5)/10)^5$ are all **FALSE**, and the numerics are
separated by factors $\approx 7$–$11$. The only $\sqrt5$ in the $4_1$
evaluation at $\mathsf b^2 = 1/5$ remains the Gauss-sum prefactor
$1/\sqrt N = 1/\sqrt5$ (pinned exactly by the parent probe).

**Verdict (scope-(a)):** the cyclic-dilogarithm product on the explicit $4_1$
data, alone, does not reproduce the icosahedral vacuum-row entries. **The GK
leg of Vector 2 closes.**

## Updated pincer verdict

Both named residues of the 2026-07-18 pincer are now decided, and both
**close at scope-(a)**:

- **Bring leg (A5):** every natural involution-twisted form has the wrong
  spectrum, and a basis-independent discriminant-class obstruction rules out
  $\mathbb Q$-congruence to the exchange form in *any* presentation.
- **GK leg (B4):** the D₅ product data live in the full quartic
  $\mathbb Q(\zeta_{30})^+$, not $\mathbb Q(\sqrt5)$, and the algebraic
  prefactor of the $1/\sqrt5$ bears no relation to the S-matrix vacuum row.

The pincer therefore **does not land**, now with both flanks exhausted rather
than merely unexplored: the exchange ceiling $1/\sqrt5$, the Gauss-sum
$1/\sqrt5$ and the icosahedral $1/\sqrt5$ remain the *same algebraic number*
with **no object-level map** — a shared normalization, exactly as the
anti-numerology gate suspected. Two genuinely new structural facts are
recorded (not interpreted): the canonical-frame universal twist carries
**golden-ratio units** $(-1\pm\sqrt5)/2$ (topological-type-universal, not
Bring-specific), and the Bring block twists carry **silver-ratio units**
$\pm(1{+}\sqrt2), \pm(\sqrt2{-}1)$ and the $\mathbb Q(\zeta_9)^+$ triple
$2\cos(2\pi k/9)$.

The magnitude scalar $m \in (0, 1/\sqrt5)$ remains **OPEN**; nothing is wired
to production. No scope-(b) exclusion is claimed anywhere in this audit: a
structural tie of the wall to level-5 geometry through some *other* mechanism
(not the involution-twisted spectra, not the D₅ product) is not excluded —
only these two named routes are, each by exact computation.

## Files

- [`computations/probes/vector2_a5_sprime_residue_probe.py`](../../computations/probes/vector2_a5_sprime_residue_probe.py)
  (+ `vector2-a5-sprime-residue.witness.json`) — 6 assertions, exit 0.
- [`computations/probes/gk_d5_cyclic_dilog_4one_probe.py`](../../computations/probes/gk_d5_cyclic_dilog_4one_probe.py)
  (+ `gk-d5-cyclic-dilog-4one.witness.json`) — 7 assertions, exit 0.
- Parent: [`computations/probes/vector2_double_pincer_probe.py`](../../computations/probes/vector2_double_pincer_probe.py)
  — its two `open_sub_items` (A5-open, B4-open) are resolved by this audit.
