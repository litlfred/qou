# Toroidal-Legendre gates (2026-07-06)

> **🛑 LANDED LATE. Gate 2 is SUPERSEDED; Gate 1 stands (added
> 2026-09-03).**
>
> **Provenance.** Written 2026-07-06, **never merged** — stranded on
> `claude/cheat-sheet-derivation-gaps-0ykco4` (tip `3409f9df39`) when
> PR #3440 merged mid-session. Restored here so both gate verdicts are
> findable by the corpus-grep checklist; until now neither was.
>
> **Gate 1 (Weinberg cosh-vs-cos) — STANDS, and is the reason to keep
> this file.** No later work has revisited the toroidal-Legendre route
> to the Weinberg gap, so without this record the "gate closed" verdict
> — including its invariant-backed scope-(b) exclusion — is invisible
> and re-derivable waste.
>
> **Gate 2 (Reeb deformation term) — SUPERSEDED by PR #3448 (bean
> `gwy3`, completed).** That work derived `g` structurally from the I1/I2
> identities with the tangent identification from the TL Markov
> property, leaving one residual CWF-functional postulate, and proved
> `pn_sign_trace_blind` sorry-free in `ReebPnMagnitude.lean`. It
> **confirms** this gate's PARTIAL finding — that the exact `g` is
> conditional on assumptions equivalent to the CWF postulate — by a
> stronger route. Cite #3448, not this section, for the live result.
>
> **Unrelated toroidal work, do not conflate:** the toroidal-harmonics
> *basis* program (branch `claude/toroidal-harmonics-basis-2026-07-06`)
> merged separately, and its Q_β tower was later **de-wired from
> production** (2026-07-19 overclaim audit). Neither event bears on the
> two gates here.

Two derive-first GATE probes asking whether toroidal Legendre functions
$Q_{\nu-1/2}(\cosh\eta)$ — the half-integer-degree Legendre functions of the
second kind, whose Heine/Fourier representation

$$
Q_{n-1/2}(\cosh\eta)
  \;=\; \int_0^{\pi} \frac{\cos(n\psi)\,d\psi}{\sqrt{2\,(\cosh\eta-\cos\psi)}}
$$

interpolates the angular ($\cos$, $\psi$) and radial ($\cosh$, $\eta$) sides
in one kernel — close known small structural gaps in the substrate
derivation chain. Both gates follow the formalize-first discipline
(`compute-author.md` §3.3): derive first, evaluate only what the derivation
prescribes, **no index/argument scanning** (CAL-4 discipline).

Corpus-grep preflight (per AGENTS.md §Before declaring "open"): no prior
toroidal-Legendre attempt exists in `docs/`, `content/`, or `computations/`
(greps for `toroidal`, `legenq`, `Q_{nu-1/2}` return only unrelated hits).
Both gates are fresh.

---

## Gate 1 — Weinberg cosh-vs-cos 1.1% gap (bean `c4uz`)

**Question.** The categorical Weinberg identity (cheat sheet §5 item 5,
commit `12b6c77c1`) is

$$
\frac{P_W}{P_Z} \;=\; \frac{\cosh(5\eta_0)}{\cosh(7\eta_0)}
\;\approx\; 0.890836
\qquad \text{vs SM } \cos\theta_W = \frac{m_W}{m_Z} \approx 0.881469,
$$

a $+1.06\%$ deviation (the cosh-vs-cos discrepancy), with
$\eta_0 = \ln q_0 \approx 0.104341$. Does the torus-saddle steepest-descent
evaluation of the $T(2,k)$ trace ratio produce, **as a derived correction**,
a $Q_{\nu-1/2}$-ratio in place of the bare cosh ratio — i.e. a principled
identity $P_W/P_Z \to Q_{5-1/2}(\cosh\eta_0)/Q_{7-1/2}(\cosh\eta_0)$ (or a
specific derived variant) closing part of the gap?

**Probe:**
[`computations/probe_toroidal_legendre_weinberg_gate.py`](../../computations/probe_toroidal_legendre_weinberg_gate.py)
→ [`probe-toroidal-legendre-weinberg-gate.witness.json`](../../computations/probe-toroidal-legendre-weinberg-gate.witness.json)
(10 assertions, all passed, 50-dps floor, cross-check tolerance $10^{-40}$).

### Derivation (what the gate actually establishes)

**(A) Exactness invariant — there is no saddle-correction series at the
$N=2$ trace level.** The trace polynomial
$P_m(h) = \mathrm{tr}_M(\sigma_1^{2m})$ is an *exact* identity in $H_2(q)$
(PR #1125 binomial pattern; re-verified sympy-exact in the probe for
$m=2$ (W $= T(2,4)$) and $m=3$ (Z $= T(2,6)$)):

$$
P_m(h) \;=\; \sum_{j=0}^{m} \tfrac{1}{2}\binom{m+j}{2j}\, h^{2j}
\;=\; \frac{q^{2m+1}+q^{-(2m+1)}}{2\,[2]_q},
\qquad h = q - q^{-1},
$$

and the $[2]_q$ cancels exactly in the ratio (sympy-verified):
$P_2/P_3 = (q^5+q^{-5})/(q^7+q^{-7})$, which at real $q_0$ **is** the cosh
ratio (probe assertion, agreement $\le 10^{-40}$). A steepest-descent
"correction" presupposes an asymptotic approximation of an integral or sum
with a large parameter; the $N=2$ Markov-trace ratio has neither — it is a
finite exact Laurent-rational function of $q$ evaluated at $q_0$. There is
no residual series in which $Q_{\nu-1/2}$ could arise as a derived
correction term. The Askey two-saddle structure
([`self-dual-higgs-real-volume.md`](../../content/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-volume.md):
torus saddle $\leftrightarrow$ Rogers $q$-ultraspherical) operates at the
**colored / large-$N$** level (colored-Jones asymptotics), one level above
the $N=2$ trace used in the W/Z identity: its saddle corrections correct
$J_N$ asymptotics, not the exact $H_2$ trace.

**(B) Monotonicity prune — the same-index bare replacement is structurally
excluded** (scope (b) per AGENTS.md §Before declaring "refuted", invariant
cited). For $x>1$ the Laplace/Heine representation (DLMF 14.12.4)

$$
Q_\nu(x) \;=\; \int_0^\infty \frac{dt}{\bigl(x+\sqrt{x^2-1}\,\cosh t\bigr)^{\nu+1}},
\qquad \nu > -1,
$$

has integrand base $x+\sqrt{x^2-1}\cosh t \ge x+\sqrt{x^2-1} > 1$ for all
$t\ge 0$, so the integrand is strictly decreasing in $\nu$ pointwise; hence
$Q_\nu(x)$ is **strictly decreasing in the degree $\nu$** at fixed argument
$x>1$. Therefore

$$
\frac{Q_{5-1/2}(\cosh\eta_0)}{Q_{7-1/2}(\cosh\eta_0)} \;>\; 1
\qquad \text{for every } \eta_0 > 0,
$$

while both targets — the categorical cosh ratio ($0.8908$) and the SM
$\cos\theta_W$ ($0.8815$) — are $< 1$. The same-index bare replacement can
never land on either target, at any substrate value. This is a one-line
structural exclusion of exactly the kind §3.3 asks for; no scan was run.

### Prescribed observation-tier evaluation (item 3, one number, no variants)

The bare ratio at $\nu = 5, 7$ evaluated at $\cosh\eta_0 = 1.0054529\ldots$,
computed by three independent routes (`mpmath.legenq` type 3, the Heine
Fourier integral, the Laplace integral; mutual agreement $\le 10^{-40}$ at
50 dps):

| quantity | value |
|---|---|
| $Q_{9/2}(\cosh\eta_0)$ | $0.88728166658966193231\ldots$ |
| $Q_{13/2}(\cosh\eta_0)$ | $0.62839571098333013447\ldots$ |
| **ratio** $Q_{9/2}/Q_{13/2}$ | $\mathbf{1.41197918935700602757}$ |
| deviation vs categorical $0.890836$ | $+58.50\%$ |
| deviation vs SM $0.881469$ | $+60.18\%$ |

(Small-$\eta$ context: as $\eta_0\to 0^+$ both $Q$'s diverge
logarithmically and the ratio tends to $1$ from above through the
digamma-offset regime $Q_{n-1/2}\approx \tfrac12\ln\tfrac{2}{x-1}-\gamma-\psi(n+\tfrac12)$;
it is $>1$ in every regime, per invariant (B).)

### Verdict

**No-reduction found (gate closed for now)** — observation tier, honest
stop. Scope calibration per AGENTS.md:

- **Excluded (scope (b), invariant cited):** the same-index bare
  replacement $Q_{5-1/2}/Q_{7-1/2}$ for $\cosh(5\eta_0)/\cosh(7\eta_0)$, by
  degree-monotonicity of $Q_\nu$ at fixed argument $>1$.
- **Not excluded (scope-limited):** toroidal-Legendre structures at the
  colored / large-$N$ saddle level — where the Askey two-saddle table
  actually operates and where a genuine steepest-descent expansion (with
  correction terms) exists — or index/argument assignments *derived* from
  such a colored-level analysis. That is a different, unprobed gate.
- The $+1.06\%$ cosh-vs-cos gap remains open; nothing here refutes
  toroidal-Legendre machinery generally.

---

## Gate 2 — the Reeb pn deformation term $(q_0-1)^2/q_0$ via toroidal harmonics (bean `de0o`)

**Question.** The landed ²H reeb-flow magnitude is
$g = 1/\sqrt{5 + (q_0-1)^2/q_0} \approx 0.446727$; the #3436 provenance audit
found the **5** derived but the deformation term **asserted** (the #3407
attack doc's "three routes" have no computational artifact). Does the
toroidal-harmonic expansion of the tube-linking/helicity kernel on the
color-tube solid torus, at aspect parameter tied to the substrate, produce
the $(q_0-1)^2/q_0$ shape as a derived correction?

**Verdict: PARTIAL** (scope-(a) throughout). Shape **and** order fall out of
a single radial identification; the exact coefficient and placement fall out
only under two further identifications that are *jointly equivalent* to the
single residual CWF postulate isolated on PR #3436 — so the toroidal route
independently **confirms** the structure and supplies a geometric
dictionary, but does **not** reduce the residual-postulate count. Probe
(12/12 assertions, 50 dps + 10 guard, tol $10^{-45}$):
[`probe_toroidal_reeb_deformation.py`](../../computations/probe_toroidal_reeb_deformation.py)
→ [`probe_toroidal_reeb_deformation.witness.json`](../../computations/probe_toroidal_reeb_deformation.witness.json).

### 2.0 Status of the inputs (what the attack doc does and does not supply)

The #3407 attack doc
([`2026-07-05-reeb-linking-operation-attack.md`](2026-07-05-reeb-linking-operation-attack.md))
supplies **no concrete integral** — Routes A/B/C have no artifact (confirmed
by the #3436 provenance audit; the probe restates the formula in one line).
The construction below is therefore a **reconstruction** from the corpus
pieces that *are* concrete: `prop:helicity-conservation` (categorical
helicity, classical limit = Gauss/Moffatt form, linking term
$2\,\mathrm{lk}_q(\varrho_i,\varrho_j)\Gamma_i^{(q)}\Gamma_j^{(q)}$) and the
color tubes as solid tori (`conj:inter-nucleon-channel-color-tube`,
`def:color-tube-fibers`).

### 2.1 Setup — two-ring kernel and its toroidal-Legendre expansion

Model the two strands of the pn bond as coaxial circular Reeb orbits $C_1$
(radius $r_1$), $C_2$ (radius $r_2$), axial separation $d$, on the
color-tube solid tori. For points at azimuthal offset $\psi$,

$$
|x - x'|^2 \;=\; r_1^2 + r_2^2 + d^2 - 2 r_1 r_2 \cos\psi
\;=\; 2 r_1 r_2\,(\chi - \cos\psi),
\qquad
\chi \;=\; \frac{r_1^2 + r_2^2 + d^2}{2 r_1 r_2},
$$

and the Coulomb/Biot–Savart kernel has the classical toroidal-Legendre
azimuthal decomposition (the Heine kernel of this doc's preamble, resummed):

$$
\frac{1}{|x - x'|}
\;=\; \frac{1}{\pi \sqrt{r_1 r_2}}
\sum_{m \ge 0} \epsilon_m \cos(m\psi)\, Q_{m-\frac{1}{2}}(\chi),
\qquad \epsilon_0 = 1,\ \epsilon_m = 2\ (m \ge 1).
$$

$\chi$ and the gauge-invariant ratio $d^2/(r_1 r_2)$ are the only scale
invariants; every toroidal-harmonic observable is a function of them alone.

### 2.2 Which geometric parameter maps to $q_0$ (the tube modulus)

**(A1) Radial identification.** The two strands sit at the bar-conjugate
radii $r_1 = v = \sqrt{q_0}$, $r_2 = v^{-1}$ in geometric-mean gauge
($r_1 r_2 = 1$) — **the strand radial ratio is the substrate deformation,
$r_1/r_2 = q_0$**. Equivalently: for coplanar coaxial circles the toroidal
separation is $\mathrm{arccosh}\,\chi|_{d=0} = \ln(r_1/r_2)$, so the
tube-modulus map is $\eta_0 = \ln q_0$ — the substrate $q$ is the
exponential of the toroidal coordinate separation of the two orbits
(matching Gate 1's $\eta_0$). This is the natural bar-involution assignment
(the $p$/$n$ strands are exchanged by $q \mapsto q^{-1}$), but it is an
**identification, not a corpus derivation**.

### 2.3 Shape and order — derived from (A1) alone

In geometric-mean gauge the invariants are $\delta = d^2$ and

$$
(r_1 - r_2)^2 \;=\; \bigl(v - v^{-1}\bigr)^2
\;=\; 2\bigl(\cosh\eta_0 - 1\bigr)
\;=\; \frac{(q_0-1)^2}{q_0}
\;=:\; \Delta ,
$$

so $\chi = \cosh\eta_0 + \delta/2 = 1 + (\Delta + \delta)/2$. Hence, given
only (A1): **the $q_0$-dependence of *any* toroidal-harmonic observable of
the two-strand configuration enters exclusively through the combination
$(q_0-1)^2/q_0$** — the deformation term's shape falls out. Bar-parity is
automatic ($\chi$ is even in $\eta_0$, symmetric under
$r_1 \leftrightarrow r_2$), and the order is

$$
\Delta = \eta_0^2 + O(\eta_0^4) = O\bigl((q_0-1)^2\bigr)
$$

(probe T1, T2, T7) — exactly the promising order the gate anticipated; the
headroom check $1 - \sqrt5\,g = \Delta/10 + O(\Delta^2)$ gives
$1.0879\times10^{-3}$ vs $\Delta/10 = 1.0897\times10^{-3}$, matching the
#3436 I2 note.

### 2.4 Exact coefficient — requires two further identifications

**(A2)** axial separation $d^2 = r_1 r_2$ ($\delta = 1$: separation =
geometric-mean radius); **(A3)** the linking magnitude is the
scale-invariant kernel amplitude at the **exchange (antipodal, $\psi=\pi$)
configuration**. Then, with $d_{\max}^2 = (r_1+r_2)^2 + d^2$ the maximal
chord between the strands,

$$
g \;=\; \sqrt{r_1 r_2}\,\frac{1}{|x-x'|}\Big|_{\psi=\pi}
\;=\; \frac{\sqrt{r_1 r_2}}{d_{\max}}
\;=\; \frac{1}{\sqrt{(v+v^{-1})^2 + 1}}
\;=\; \frac{1}{\sqrt{5 + \Delta}}
$$

**exactly** (T3; the last step is I1 of #3436:
$5 + (v-v^{-1})^2 = 1 + (v+v^{-1})^2$). In toroidal harmonics this is the
alternating full tower at $\chi = \cosh(\ln q_0) + \tfrac12$:

$$
\frac{1}{\sqrt{5 + \frac{(q_0-1)^2}{q_0}}}
\;=\; \frac{1}{\pi}\sum_{m\ge0} \epsilon_m (-1)^m\,
Q_{m-\frac{1}{2}}\!\Bigl(\cosh(\ln q_0) + \tfrac12\Bigr),
$$

verified to $3.9\times10^{-62}$ (T4, 300 terms). Two structural bonuses:
the **elliptic modulus** of the two-ring kernel is exactly twice the landed
magnitude, $k = 2g$, via the classical closed form
$Q_{1/2}(\chi) = (\tfrac2k - k)K(k) - \tfrac2k E(k)$ (T5); and the classical
limit $q \to 1$ gives $\chi = \tfrac32$, $g = 1/\sqrt5$ with
$5 = (r_1+r_2)^2 + d^2 = 2^2 + 1^2$ (T8) — the same $1^2 + 2^2$
decomposition as the derived $|\mu_{\min}|^2$ of the sign-pattern route,
with dictionary: pn-degree $2 \mapsto r_1 + r_2$ (deforming to $[2]_v$,
matching I2's $2 \to [2]_v$) and pp−nn asymmetry $1 \mapsto d$ (undeformed,
matching I2's undeformed diagonal).

### 2.5 What the expansion does *not* do (honest negatives)

1. **The helicity integral proper does not select $g$.** For two closed
   coaxial filaments the mutual helicity term is the Neumann functional
   $\oint\oint dl\cdot dl'/|x-x'|$, which picks the **$m=1$ mode alone**:
   $Q_{1/2}(\chi)/\pi \approx 0.124168 \ne g \approx 0.446727$ (T6,
   $\sim3.6\times$ off). Moreover coaxial parallel circles have Gauss
   $\mathrm{lk} = 0$, so $g$ is not a literal Gauss linking number of this
   configuration. $g$ arises as the *exchange-point amplitude* (the full
   alternating tower), not as the helicity mode — the toroidal route does
   **not** derive $g$ from `prop:helicity-conservation`'s integral as-is.
   Scope-(a): this evaluates one concrete mode of one configuration; no
   structural exclusion of helicity-type functionals is claimed.
2. **(A2)+(A3) are jointly equivalent to the #3436 residual postulate.**
   The antipodal chord has direction $(r_1+r_2,\, d) = ([2]_v,\, 1)$, so its
   inclination satisfies $\tan\theta = 1/[2]_v = z$ and $g = \sin\theta$ —
   precisely I3 (sine of the channel-space direction $(1, z)$). The
   toroidal picture *geometrically realizes* the CWF unit-tangent postulate;
   it does not replace it. Within the toroidal picture the "$1$"
   ($d^2 = r_1 r_2$) is un-derived; via the I2 dictionary it corresponds to
   the *derived* pp−nn asymmetry entry, so the picture is consistent with —
   but parasitic on — the algebraic derivation chain of #3436 §2b–§2d.

### Verdict

**PARTIAL** — the gate's target order was right and the shape is forced:

- **Derived (unconditional given A1):** the deformation enters only as
  $(q_0-1)^2/q_0$, at order $O((q_0-1)^2)$, bar-parity automatic; tube
  modulus $\eta_0 = \ln q_0$; toroidal argument
  $\chi = \cosh(\ln q_0) + \tfrac12$.
- **Conditional (A2+A3 $\equiv$ the #3436 CWF postulate):** the exact
  landed magnitude $g = 1/\sqrt{5+\Delta} = \sqrt{r_1 r_2}/d_{\max} = k/2$,
  with the toroidal-Legendre tower identity of §2.4.
- **Negative, scope-(a):** the $m=1$ mutual-helicity mode of this
  configuration, alone as evaluated here, does not produce $g$.
- **No fits, no new constants, no $(d, \psi)$ scanning** beyond the
  preregistered configuration (Rule-14 / CAL-4 discipline, as Gate 1).

Net: the toroidal-harmonic route lands on the same one-postulate frontier
as #3436's CWF route, independently confirming the structure and adding the
geometric dictionary plus the negative helicity-mode finding. Coordination:
PR #3436 (bean `gwy3`) notified.
