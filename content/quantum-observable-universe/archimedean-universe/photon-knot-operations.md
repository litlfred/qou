This document translates and summarises the photon–photon pair production
algebra from the paper into a documentation-friendly form.  It maps each
torus knot operator $T_{m,n}$ to the Hecke normal form (NF) produced when
it acts on two colored photons, and aligns the results with the
knot–particle dictionary
([Remark 4.25.4](#rem:knot-particle-dictionary)).

**Paper reference.**
Canonical NF decompositions for all knot operators are given in the paper.
The tables here summarise, translate, and cross-reference that algebra;
they do not restate full derivations.

**Witness code.**
The corresponding NF computations are implemented and witnessed in:
- [`folio-assistant/computations/pair-production.py`](../../../../folio-assistant/computations/pair-production.py)
- [`folio-assistant/computations/pair-production-nf.py`](../../../../folio-assistant/computations/pair-production-nf.py)
- [`folio-assistant/computations/pair-production.witness.json`](../../../../folio-assistant/computations/pair-production.witness.json)

---

## Notation

**Colored photon.**
A photon with color content (polarization dressing) is the Hecke algebra
element

$$
  \gamma_i = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
  \quad \in H_3(q)
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$ are independent
color weights, $\sigma_0$ acts on the $(\sigma, r)$ crossing plane,
$\sigma_1$ acts on the $(r, g)$ crossing plane, and
$\sigma_0\sigma_1 = L_+$ is the Hopf link dressing.  The subscript $i$
distinguishes distinct photons ($\gamma_1, \gamma_2$) from the NF basis
element $\gamma = \mathbf{1}$ (the bare photon identity).

The **3-term specialization** $\varphi_{01} = 0$ (no Hopf dressing)
recovers the form used in the existing pair production derivations
([Breit–Wheeler pair production](#def:breit-wheeler-pair-production),
[color content](#rem:knot-basis-color-content)).  The general 4-term form
is needed when the photon carries inherent Hopf link content.

**NF basis of $H_3(q)$.**
Every element of $H_3(q)$ reduces to a unique linear combination of the
six basis elements

$$
  \{\gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\}
  \quad \text{where} \quad
  \gamma = \mathbf{1},\
  L_+ = \sigma_0\sigma_1,\
  L_- = \sigma_1\sigma_0,\
  e^- = \sigma_0\sigma_1\sigma_0.
$$

See [particle NF table](#rem:particle-nf-table) for the full decomposition
of each fundamental particle.

**Hecke reduction rules.**
$$
  \sigma_i^2 = h\sigma_i + \mathbf{1},
  \qquad
  \sigma_i^{-1} = \sigma_i - h\mathbf{1},
  \qquad
  h = q - q^{-1} \approx 0.2091 \text{ at } q_0.
$$

**Torus knot operator.**
A torus knot operator $T_{m,n}$ acts on a photon pair by insertion
between the two photons:

$$
  P_{T_{m,n}} = \gamma_1 \cdot \beta(T_{m,n}) \cdot \gamma_2
$$

where $\beta(T_{m,n})$ is the standard braid word for $T_{m,n}$ in
$H_3(q)$, and the product is reduced to NF.

---

## Witnessed NF decompositions

Throughout this section, we write
$\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
+ \varphi_{01}\sigma_0\sigma_1$
and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1
+ \psi_{01}\sigma_0\sigma_1$.

### $T_{1,0}$ — trivial knot (vacuum)

**Braid word:** $\beta = \mathbf{1}$.

$$
  P_{T_{1,0}} = \gamma_1 \cdot \gamma_2
$$

This is the colored-photon pair product.  Expanding all $4 \times 4 = 16$
terms and applying the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$,
the Yang–Baxter relation $\sigma_1\sigma_0\sigma_1 = e^-$, and the
product $(\sigma_0\sigma_1)^2 = L_- + he^-$:

$$
  \mathrm{NF}(P_{T_{1,0}})
  =
  (1 + \varphi_0\psi_0 + \varphi_1\psi_1)\gamma
  + (\varphi_0 + \psi_0 + \varphi_0\psi_0 h + \varphi_{01}\psi_1)\sigma_0
  + (\varphi_1 + \psi_1 + \varphi_1\psi_1 h + \varphi_0\psi_{01})\sigma_1
  + (\varphi_{01} + \psi_{01} + \varphi_0\psi_1
     + h(\varphi_0\psi_{01} + \varphi_{01}\psi_1))L_+
  + (\varphi_1\psi_0 + \varphi_{01}\psi_{01})L_-
  + (\varphi_{01}\psi_0 + \varphi_1\psi_{01}
     + \varphi_{01}\psi_{01} h)e^-
$$

**Key observation: the $e^-$ channel is nonzero when either photon
carries Hopf link dressing** ($\varphi_{01} \neq 0$ or $\psi_{01} \neq 0$).
Physically, the Hopf content of one photon ($\sigma_0\sigma_1$) combines
with crossing content of the other ($\sigma_0$ or $\sigma_1$) to form
trefoils:

- $L_+ \cdot \sigma_0 = \sigma_0\sigma_1\sigma_0 = e^-$
  (Hopf link plus crossing equals trefoil)
- $\sigma_1 \cdot L_+ = \sigma_1\sigma_0\sigma_1 = e^-$
  (via Yang–Baxter)

In the **3-term specialization** ($\varphi_{01} = \psi_{01} = 0$),
the formula reduces to the 5-term pair product with no $e^-$ channel:

$$
  (1 + \varphi_0\psi_0 + \varphi_1\psi_1)\gamma
  + (\varphi_0 + \psi_0 + \varphi_0\psi_0 h)\sigma_0
  + (\varphi_1 + \psi_1 + \varphi_1\psi_1 h)\sigma_1
  + \varphi_0\psi_1 L_+
  + \varphi_1\psi_0 L_-
$$

matching the canonical derivation in
[Breit–Wheeler pair production](#def:breit-wheeler-pair-production).

**Produced channels:** all six basis elements when $\varphi_{01}$ or
$\psi_{01} \neq 0$; five (no $e^-$) in the 3-term specialization.

**$L_+/L_-$ asymmetry.**  The $L_+$ coefficient has five contributing
terms versus two for $L_-$.  This is because the photon's Hopf term
is $\sigma_0\sigma_1 = L_+$ (not $L_-$), so it preferentially feeds
the $L_+$ channel via direct contributions and Hecke corrections.

---

### $T_{2,1}$ — single Hopf crossing

**Braid word:** $\beta = \sigma_0$.

$$
  P_{T_{2,1}} = \gamma_1 \cdot \sigma_0 \cdot \gamma_2
$$

First, $\gamma_1 \cdot \sigma_0 = \varphi_0\mathbf{1}
+ (1 + \varphi_0 h)\sigma_0 + \varphi_1 L_- + \varphi_{01} e^-$.
Multiplying by $\gamma_2$ and reducing to NF, the **3-term
specialization** ($\varphi_{01} = \psi_{01} = 0$) gives:

$$
  \mathrm{NF}(P_{T_{2,1}})\big|_{\varphi_{01}=\psi_{01}=0}
  =
  (\varphi_0 + \psi_0 + \varphi_0\psi_0 h)\gamma
  + (1 + \varphi_0\psi_0 + \varphi_0 h + \psi_0 h
     + \varphi_0\psi_0 h^2)\sigma_0
  + (\varphi_0\psi_1 + \varphi_1\psi_0)\sigma_1
  + (\psi_1 + \varphi_0\psi_1 h)L_+
  + (\varphi_1 + \varphi_1\psi_0 h)L_-
  + \varphi_1\psi_1 e^-
$$

The $e^-$ coefficient is $\varphi_1\psi_1$ — the degree-3 trefoil channel
opens when **both** photons carry $\sigma_1$ color content.  This arises
from $\varphi_1\sigma_1 \cdot \sigma_0 \cdot \psi_1\sigma_1
= \varphi_1\psi_1\sigma_1\sigma_0\sigma_1 = \varphi_1\psi_1 e^-$
via Yang–Baxter.

In the **general 4-term form**, the $e^-$ coefficient becomes
$\varphi_1\psi_1 + \varphi_{01}
+ h(\varphi_0\varphi_{01} + \varphi_1\psi_{01}
+ \psi_0\varphi_{01} + \psi_{01}\varphi_1)
+ h^2\varphi_{01}\psi_{01}$,
acquiring additional contributions from Hopf dressing.

**Produced channels:** $\gamma$, $\sigma_0$, $\sigma_1$, $L_+$, $L_-$,
$e^-$ (present if $\varphi_1\psi_1 \neq 0$ in the 3-term case; always
present in the 4-term case when $\varphi_{01} \neq 0$).

---

### $T_{2,2}$ — Hopf link (double crossing)

**Braid word:** $\beta = \sigma_0^2$.

Applying the Hecke relation immediately:

$$
  \sigma_0^2 = h\sigma_0 + \mathbf{1}
$$

Therefore

$$
  P_{T_{2,2}}
  = \gamma_1 \cdot (h\sigma_0 + \mathbf{1}) \cdot \gamma_2
  = h \cdot P_{T_{2,1}} + P_{T_{1,0}}
$$

The NF is a linear combination of the $T_{2,1}$ and $T_{1,0}$ operators
with weight $h \approx 0.209$.  **No new basis elements appear beyond those
already present in $P_{T_{1,0}}$ and $P_{T_{2,1}}$.**

In particular: the Hecke relation exhausts the degree-2 structure of
$\sigma_0^2$ before any degree-3 (trefoil) term can form independently.
The Hopf link $T_{2,2}$ links two loops but does not entangle them as a
trefoil, which requires three crossings involving both $\sigma_0$ and
$\sigma_1$.

**Produced channels:** $\gamma$, $\sigma_0$, $\sigma_1$, $L_+$, $L_-$,
and $e^-$ only via the $T_{2,1}$ sub-result (weighted by $h$) plus the
$T_{1,0}$ Hopf dressing contribution.  No new trefoil content independent
of those two.

---

### $T_{2,3}$ — trefoil (electron)

**Braid word:** $\beta = \sigma_0\sigma_1\sigma_0$.

$$
  P_{T_{2,3}} = \gamma_1 \cdot \sigma_0\sigma_1\sigma_0 \cdot \gamma_2
$$

The braid word $\sigma_0\sigma_1\sigma_0$ is itself the basis element
$e^- \in H_3(q)$.  In the **3-term specialization**:

$$
  \mathrm{NF}(P_{T_{2,3}})\big|_{\varphi_{01}=\psi_{01}=0}
  = \psi_1\varphi_1\sigma_0
  + \psi_0\varphi_0\sigma_1
  + c_+ L_+
  + c_- L_-
  + c_{e^-} e^-
$$

with

$$
  c_{e^-} = 1
  + h(\varphi_0 + \varphi_1 + \psi_0 + \psi_1)
  + h^2(\varphi_0\psi_0 + \varphi_0\psi_1 + \varphi_1\psi_0 + \varphi_1\psi_1)
  + \varphi_0\psi_1 + \varphi_1\psi_0.
$$

The $\gamma$ coefficient is **zero** and the $e^-$ coefficient has
constant term $1$: the trefoil operator always produces electron content
and annihilates the vacuum channel.  This is the process that produces
an electron in the categorical model.

**Produced channels:** all six — $\sigma_0$, $\sigma_1$, $L_+$, $L_-$,
$e^-$ (always present); $\gamma$ reappears when $\varphi_{01}\psi_{01}
\neq 0$ in the 4-term form.

---

### $T_{2,5}$ — cinquefoil (muon / bottom quark)

**Braid word:** $\beta = (\sigma_0\sigma_1)^2\sigma_0$.

The cinquefoil word has length 5; after NF reduction via iterated
Hecke relations all six basis elements of $H_3(q)$ can appear.

$$
  P_{T_{2,5}} = \gamma_1 \cdot (\sigma_0\sigma_1)^2\sigma_0 \cdot \gamma_2
$$

The degree-3 $e^-$ content is present (inherited from the three-crossing
core of the word), along with $L_\pm$ from the Hopf-link subwords.

Per [Remark 4.25.4](#rem:knot-particle-dictionary): $T_{2,5}$ corresponds
to the **bottom quark** $\mathfrak{b}$ (positive crossing, generation 2,
lepton partner $\mu^-$); its mirror $T_{2,5}^\sigma$ corresponds to
**strange** $\mathfrak{s}$ (negative crossing orientation, mirror of
$\mu^-$).  These are second-generation particles; $T_{2,5}$ is not
strange.

**Produced channels:** all six basis elements; degree-3 content present.

---

### $T_{3,5}$ — weak force vertex (open)

**Braid word:** $\beta = (\sigma_0\sigma_1)^5$.

This is the $(3,5)$ torus knot on 3 strands ($B_3$), with 10 crossings
(knot $10_{124}$).

Per [knot–particle dictionary](#rem:knot-particle-dictionary) Table 1:
$T_{3,5}$ is associated with the **weak force**
($\beta$-decay vertex), not with any quark or lepton generation.  It is
**not** strange ($\mathfrak{s}$) or bottom ($\mathfrak{b}$); those are
$T_{2,5}^\sigma$ and $T_{2,5}$ respectively.

The full NF of $\gamma_1 \cdot (\sigma_0\sigma_1)^5 \cdot \gamma_2$ in
$H_3(q)$ involves all basis elements; the physical identification of the
specific production channel is an open question in the current
paper.

**Produced channels:** all six basis elements; physical
interpretation beyond the weak-force candidate is open.

---

## Summary table

The table below maps each torus knot operator to its NF content and
physical channel, aligned with the knot–particle dictionary
([Remark 4.25.4](#rem:knot-particle-dictionary)).

| Knot | Braid word $\beta$ | NF basis elements produced | $e^-$ present? | Particle / channel |
|------|-------------------|---------------------------|:--------------:|-------------------|
| $T_{1,0}$ | $\mathbf{1}$ | $\gamma, \sigma_0, \sigma_1, L_+, L_-$ (+ $e^-$ if Hopf-dressed) | 4-term only | Vacuum / photon (trivial) |
| $T_{2,1}$ | $\sigma_0$ | all six | if $\varphi_1\psi_1 \neq 0$ | Single Hopf crossing; lepton seed conditional on color |
| $T_{2,2}$ | $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ | as $h \cdot T_{2,1} + T_{1,0}$ | conditional | Hopf link; no independent trefoil channel |
| $T_{2,3}$ | $\sigma_0\sigma_1\sigma_0$ | all six | **always** (coeff $\geq 1$) | Electron $e^-$ / up quark $\mathfrak{u}$ (gen. 1) |
| $T_{2,5}$ | $(\sigma_0\sigma_1)^2\sigma_0$ | all six | yes | Bottom quark $\mathfrak{b}$ / muon $\mu^-$ (gen. 2) |
| $T_{3,5}$ | $(\sigma_0\sigma_1)^5$ | all six | yes | Weak-force vertex; $\beta$-decay mediator (channel open) |

---

## Alignment with Remark 4.25.4

Remark 4.25.4 ([knot–particle dictionary](#rem:knot-particle-dictionary))
gives the following quark assignment (Table 4):

| Quark | Braid element in $\mathcal{B}_3$ | Lepton descent | Generation |
|-------|----------------------------------|---------------|:----------:|
| Up $\mathfrak{u}$ | $\sigma_i$ (positive crossing) | $\leftarrow T_{2,3}$ | 1 |
| Down $\mathfrak{d}$ | $\sigma_i^{-1}$ (negative crossing) | $\leftarrow T_{2,3}^\sigma$ | 1 |
| Strange $\mathfrak{s}$ | $\sigma_i^{-1}$ (negative crossing) | $\leftarrow T_{2,5}^\sigma$ | 2 |
| Charm $\mathfrak{c}$ | $\sigma_i$ (positive crossing) | $\leftarrow T_{2,7}$ | 3 |
| Bottom $\mathfrak{b}$ | $\sigma_i$ (positive crossing) | $\leftarrow T_{2,5}$ | 2 |
| Hopf${}^2$ color $\mathfrak{t}$ | — | $\leftarrow T_{3,4}$ | — |

**Key alignment points:**

1. **Up and down quarks both descend from generation-1 torus knots.**
   $\mathfrak{u} \leftarrow T_{2,3}$ (positive crossing, $\sigma_i$)
   and $\mathfrak{d} \leftarrow T_{2,3}^\sigma$ (negative crossing,
   $\sigma_i^{-1}$).  The mirror relationship $T_{2,3} \leftrightarrow
   T_{2,3}^\sigma$ encodes the up/down flavour difference as crossing
   orientation, not knot type.  Whether this orientation corresponds
   to matter/antimatter or up/down flavour is a model-dependent
   interpretation; the paper assigns it to flavour.

2. **$T_{2,5}$ is bottom, not strange.**
   $T_{2,5}$ (positive crossing, generation 2) → bottom $\mathfrak{b}$,
   lepton partner $\mu^-$.  Its mirror $T_{2,5}^\sigma$ (negative
   crossing) → strange $\mathfrak{s}$.

3. **$T_{3,5}$ is not a quark or lepton.**
   Per Table 1 of the dictionary, $T_{3,5}$ ($10_{124}$) is the weak
   force / $\beta$-decay vertex, not assigned to any fermion generation.
   It is included in the photon operator table above as an
   open-channel entry.

4. **$T_{2,2}$ (Hopf link) is a link, not a knot (boson sector).**
   Per Table 2 of the dictionary, $T(2,2)$ is a 2-component link whose
   closure is the gluon $L_\pm$.  In the photon operator context,
   $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ decomposes it into the $T_{2,1}$
   and $T_{1,0}$ channels with weight $h$; no independent trefoil
   production occurs.

---

## 3-term vs 4-term photon: impact on pair production

The existing pair production derivations
([Breit–Wheeler](#def:breit-wheeler-pair-production),
[color content](#rem:knot-basis-color-content),
[quark–antiquark production](#def:quark-antiquark-production))
use the 3-term photon $\gamma_i = \mathbf{1} + \varphi_0\sigma_0
+ \varphi_1\sigma_1$ (i.e., $\varphi_{01} = 0$).

The 4-term form
$\gamma_i = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
+ \varphi_{01}\sigma_0\sigma_1$
adds Hopf link dressing to the photon.  Its main consequences:

- **$T_{1,0}$ (trivial): $e^-$ channel opens.**
  Even without a knot operator, Hopf-dressed photons produce trefoil
  content via $L_+ \cdot \sigma_0 = e^-$ and
  $\sigma_1 \cdot L_+ = e^-$.

- **$T_{2,1}$ (Hopf crossing): $e^-$ always present.**
  In the 3-term case, $e^-$ requires $\varphi_1\psi_1 \neq 0$.
  In the 4-term case, $e^-$ is present whenever $\varphi_{01} \neq 0$,
  even if $\varphi_1 = \psi_1 = 0$.

- **$L_+/L_-$ asymmetry amplified.**
  The photon's Hopf term $\varphi_{01}L_+$ directly feeds the $L_+$
  channel; the $L_-$ channel only receives cross-color and self-Hopf
  products.

The 3-term derivations remain valid as the $\varphi_{01} = 0$
specialization of the general 4-term formula.
