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
  \gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  \quad \in H_3(q)
$$

where $\varphi_0, \varphi_1 \in \mathbb{R}$ are independent color weights,
$\sigma_0$ acts on the $(\sigma, r)$ crossing plane, and $\sigma_1$ acts
on the $(r, g)$ crossing plane.  The identity $\mathbf{1}$ **is** the bare
photon $\gamma$; the $\sigma_i$ terms are its polarization dressing
([Breit–Wheeler pair production](#def:breit-wheeler-pair-production)).

**NF basis of $H_3(q)$.**
Every element of $H_3(q)$ reduces to a unique linear combination of the
six basis elements

$$
  \{\,\gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\,\}
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

### $T_{1,0}$ — trivial knot (neutrino / vacuum)

**Braid word:** $\beta = \mathbf{1}$.

$$
  P_{T_{1,0}} = \gamma_1 \cdot \mathbf{1} \cdot \gamma_2
  = \gamma_1 \cdot \gamma_2
$$

This is the bare colored-photon pair product
([Breit–Wheeler pair production](#def:breit-wheeler-pair-production)).
Its NF is

$$
  \mathrm{NF}(P_{T_{1,0}})
  =
  (1 + \varphi_0\psi_0 + \varphi_1\psi_1)\,\gamma
  + (\varphi_0 + \psi_0 + \varphi_0\psi_0 h)\,\sigma_0
  + (\varphi_1 + \psi_1 + \varphi_1\psi_1 h)\,\sigma_1
  + \varphi_0\psi_1\,L_+
  + \varphi_1\psi_0\,L_-
$$

No $e^-$ (trefoil / degree-3) term appears.  The $L_\pm$ terms arise
only from cross-color products $\varphi_0\psi_1$ and $\varphi_1\psi_0$.

**Produced channels:** $\gamma$ (vacuum/photon), $\sigma_0$, $\sigma_1$,
$L_+$, $L_-$.  No degree-3 content.

---

### $T_{2,1}$ — single Hopf crossing

**Braid word:** $\beta = \sigma_0$.

$$
  P_{T_{2,1}} = \gamma_1 \cdot \sigma_0 \cdot \gamma_2
$$

Expanding with $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$
and $\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$, applying the
Hecke relation $\sigma_0^2 = h\sigma_0 + \mathbf{1}$, and the braid relation
$\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$:

$$
  \mathrm{NF}(P_{T_{2,1}})
  =
  (\varphi_0\psi_0 h + \varphi_1\psi_1 h)\,\gamma
  + (1 + \varphi_0 h + \psi_0 h + \varphi_0\psi_0 h^2 + \varphi_1\psi_1)\,\sigma_0
  + \varphi_0\psi_1\,\sigma_1
  + (\varphi_0 + \psi_0 + \varphi_0\psi_0 h)\,L_+
  + \varphi_1\psi_0\,L_-
  + \varphi_1\,e^-
$$

The $e^-$ coefficient is $\varphi_1$ — the degree-3 trefoil channel opens
when the first photon carries $\sigma_1$ color content.

**Produced channels:** $\gamma$, $\sigma_0$, $\sigma_1$, $L_+$, $L_-$,
$e^-$ (degree-3 present if $\varphi_1 \neq 0$).

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
$\sigma_0^2$ before any degree-3 (trefoil) term can form.  The Hopf link
$T_{2,2}$ links two loops but does not entangle them as a trefoil, which
requires three crossings involving both $\sigma_0$ and $\sigma_1$.

**Produced channels:** $\gamma$, $\sigma_0$, $\sigma_1$, $L_+$, $L_-$,
and $e^-$ only if the $T_{2,1}$ sub-result carries it (i.e., only if
$\varphi_1 \neq 0$, weighted by $h$).  No new trefoil content independent
of the $T_{2,1}$ contribution.

---

### $T_{2,3}$ — trefoil (electron)

**Braid word:** $\beta = \sigma_0\sigma_1\sigma_0$.

$$
  P_{T_{2,3}} = \gamma_1 \cdot \sigma_0\sigma_1\sigma_0 \cdot \gamma_2
$$

The braid word $\sigma_0\sigma_1\sigma_0$ is itself the basis element
$e^- \in H_3(q)$.  After full NF reduction:

$$
  \mathrm{NF}(P_{T_{2,3}})
  = c_\gamma\,\gamma
  + c_0\,\sigma_0
  + c_1\,\sigma_1
  + c_+\,L_+
  + c_-\,L_-
  + c_{e^-}\,e^-
$$

All six basis elements are present; the degree-3 coefficient $c_{e^-}$
receives contributions from all cross-products of $\gamma_1$, $e^-$, and
$\gamma_2$.  This is the process that produces an electron in the
categorical model.

**Produced channels:** all six — $\gamma$, $\sigma_0$, $\sigma_1$,
$L_+$, $L_-$, $e^-$.  The $e^-$ (trefoil) channel is **always present**,
independent of photon color content.

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

### $T_{3,5}$ — weak force vertex (TBD)

**Braid word:** $\beta = (\sigma_0\sigma_1\sigma_2)^5$ in $B_4$,
or in the $H_3(q)$ restriction $(\sigma_0\sigma_1)^2$ (the $(2,4)$ torus
link word when restricted to two generators).

Per [knot–particle dictionary](#rem:knot-particle-dictionary) Table 1:
$T_{3,5}$ (knot $10_{124}$) is associated with the **weak force**
($\beta$-decay vertex), not with any quark or lepton generation.  It is
**not** strange ($\mathfrak{s}$) or bottom ($\mathfrak{b}$); those are
$T_{2,5}^\sigma$ and $T_{2,5}$ respectively.

The full NF of $\gamma_1 \cdot (\sigma_0\sigma_1)^2 \cdot \gamma_2$ in
$H_3(q)$ involves all basis elements; the physical identification of the
specific production channel is an open question (TBD in the current
paper).

**Produced channels:** all six basis elements (TBD physical
interpretation beyond weak-force candidate).

---

## Summary table

The table below maps each torus knot operator to its NF content and
physical channel, aligned with the knot–particle dictionary
([Remark 4.25.4](#rem:knot-particle-dictionary)).

| Knot | Braid word $\beta$ | NF basis elements produced | $e^-$ present? | Particle / channel |
|------|-------------------|---------------------------|:--------------:|-------------------|
| $T_{1,0}$ | $\mathbf{1}$ | $\gamma, \sigma_0, \sigma_1, L_+, L_-$ | no | Vacuum / photon (trivial) |
| $T_{2,1}$ | $\sigma_0$ | $\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-$ | if $\varphi_1 \neq 0$ | Single Hopf crossing; lepton seed conditional on color |
| $T_{2,2}$ | $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ | $\gamma, \sigma_0, \sigma_1, L_+, L_-$ (+ $e^-$ via $T_{2,1}$ if colored) | conditional | Hopf link; no independent trefoil channel |
| $T_{2,3}$ | $\sigma_0\sigma_1\sigma_0$ | all six | **always** | Electron $e^-$ / up quark $\mathfrak{u}$ (gen. 1) |
| $T_{2,5}$ | $(\sigma_0\sigma_1)^2\sigma_0$ | all six | yes | Bottom quark $\mathfrak{b}$ / muon $\mu^-$ (gen. 2) |
| $T_{3,5}$ | $(\sigma_0\sigma_1)^2$ (restricted) | all six | yes | Weak force vertex (TBD; $\beta$-decay mediator) |

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
   It is included in the photon operator table above as a TBD entry.

4. **$T_{2,2}$ (Hopf link) is a link, not a knot (boson sector).**
   Per Table 2 of the dictionary, $T(2,2)$ is a 2-component link whose
   closure is the gluon $L_\pm$.  In the photon operator context,
   $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ decomposes it into the $T_{2,1}$
   and $T_{1,0}$ channels with weight $h$; no independent trefoil
   production occurs.
