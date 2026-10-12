# Υ(1S) at 14 crossings: what the dictionary's meson construction gives

Bean `qou-eo5q`. Owner decision 3a (ofri, 2026-10-10): **keep** the "Meson at
$2n$ crossings" relabel of `prop:lepton-meson-torus-knot-dictionary` and do
**not** add Υ to the table. Also, **try to compute** the generation-3
quarkonium Υ = $b\bar b$ entry with exactly the construction the existing
meson entries use, and report the residual. Nothing was fitted.

Probe: [`computations/eightfold/upsilon_14_crossing_probe.py`](../../computations/eightfold/upsilon_14_crossing_probe.py),
witness `computations/eightfold/upsilon-14-crossing-probe.witness.json`
(5/5 checks). Proton pin $q_0 = 1.1099785827513808\ldots$, mpmath at 70 dps,
exact `Fraction` Seifert ratios.

## 1. The construction

The only producer of meson values in this arc is the Hecke-character ×
Seifert-ratio formula of `prop:meson-kaon-pion-hecke-seifert` (row $n=5$) and
`prop:gen3-meson-phi-hecke-seifert` (row $n=7$), implemented in
`computations/meson_gen3_eta_phi.py`:

$$
\frac{m_X}{m_\pi} = \chi^{(2,1)}(\sigma_1^n)\,\Bigl(\frac{V_S(T(2,n))}{V_S(T(2,3))}\Bigr)^{2},
\qquad \chi^{(2,1)}(\sigma_1^n) = q^n + (-q^{-1})^n,
\qquad V_S(T(2,n)) = \frac{\pi(n-2)}{n}\ (n \text{ odd}).
$$

The index $n$ is the **torus knot of the row** ($\pi$ is the unit at $n=3$,
$K$ at $n=5$, the generation-3 slot at $n=7$). It is **not** the meson's
constituent crossing total: $K = \bar u s$ is $3+5 = 8$ crossings and is
evaluated at $n=5$, and the $n=7$ slot is identified with $\phi = s\bar s$,
whose constituents are both $T(2,5)$.

Controls at the proton pin: $m_K/m_\pi$ predicted $3.536094$ against PDG
$3.537118$ ($-290$ ppm), and the $n=7$ slot gives $7.320105$ against
$m_\phi/m_\pi = 7.304279$ ($+0.22\,\%$). Both reproduce the published rows.

Target: $m_{\Upsilon(1S)}/m_{\pi^\pm} = 9460.30(26)/139.57039 = 67.7816 \pm 0.0019$.

## 2. Reading R1: generation index, $n = 7$. Defined with no new choice.

$b = T(2,7)^\sigma$, so $\Upsilon = b\bar b$ lives in the generation-3 slot. The
mirror replaces $\sigma_1$ by $\sigma_1^{-1}$ (eigenvalues $q^{-1}$, $-q$) and
only flips the sign of $\chi$, so $|m_X/m_\pi|$ is unchanged:

| | value |
|---|---|
| predicted $m_X/m_\pi$ | $7.32011$ |
| PDG $m_\Upsilon/m_\pi$ | $67.7816$ |
| relative residual | **$-89.20\,\%$** |

The value is exactly the $\phi$ slot. The construction takes one knot index,
not two constituents, so it **cannot tell $\phi$ from Υ**. The same holds one
row down: it cannot tell $K = \bar u s$ from $\phi = s\bar s$ at $n = 5$.

## 3. Reading R2: crossing count, $n = 14$. Not defined. One choice is missing.

$\chi^{(2,1)}(\sigma_1^{14}) = q^{14} + q^{-14} = 4.54133$ follows from the
same Hoefsmit derivation and involves no choice. **The missing choice is the
Seifert volume $V_S(T(2,14))$.** $T(2,14)$ is a 2-component **link**, and the
corpus defines $V_S(T(2,n))$ only for torus **knots**, through the Euler
number $e = 1 - \tfrac12 - \tfrac1n$ for odd $n$. The construction stops here.

To show that no obvious extension rescues it, two candidates are evaluated as
**diagnostics only**. Neither is the construction and neither is adopted.
Picking between them by residual would be selection against the target (§NO
FITTING).

| extension (not adopted) | Seifert ratio | $m_X/m_\pi$ | residual |
|---|---|---|---|
| R2a: literal $\pi(n-2)/n$ at $n=14$ | $18/7$ | $30.028$ | $-55.7\,\%$ |
| R2b: $2\pi\lvert\chi_{\mathrm{orb}}\rvert$ of the link's base ($S^2$ minus 2 points, one cone point of order 7) | $36/7$ | $120.11$ | $+77.2\,\%$ |

The Seifert ratio needed to reach the target would be $3.8634$, which neither
geometric candidate produces. This is recorded as a size, not as a
proposal.

## 4. Verdict, scope (a)

**Scope-(a) negative.** The dictionary's meson construction, used alone and
as it stands, does not reproduce $m_\Upsilon/m_\pi$. Under the only reading
that needs no new choice ($n=7$) it returns the $\phi$ value, $-89\,\%$ against
Υ. Under the 14-crossing reading it is undefined until a Seifert volume for the
torus link $T(2,14)$ is supplied. This says nothing about whether a
heavy-quarkonium term could enter some other construction. No invariant
excludes one, so no scope-(b) claim is made.

## 5. A defect in the relabel, found while checking it. Not edited.

The relabelled header reads "Meson at $2n$ crossings" and the block says the
meson in row $n$ has total crossing number $2n = 2(2k+1)$. Using the block's
own `-proof` crossing counts:

| row $n$ | $2n$ | listed meson | its crossings |
|---|---|---|---|
| 3 | 6 | $\pi = \bar u d$ | 6 ✓ |
| 5 | 10 | $K = \bar u s$ | **8** |
| 7 | 14 | $\phi = s\bar s$ | **10** |

The header holds only in row 1. The column actually follows the ladder
$6, 8, 10 = n + 3$. Read literally, the $2n$ rule would put $\phi$ ($10$) in
row 5 and Υ ($14$) in row 7. That is the repopulation the owner declined.
The owner ruled to keep the relabel as is, so this note only records the
mismatch and changes nothing. Bean `qou-eo5q` carries the options.
