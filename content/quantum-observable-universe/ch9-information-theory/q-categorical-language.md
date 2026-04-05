The **first-order language of rigid monoidal categories**
$\mathcal{L}_{\mathrm{RMC}}$ is a multi-sorted first-order language
with the following signature:

**Sorts.**

- $\mathrm{Ob}$ — objects of the category
- $\mathrm{Mor}(X, Y)$ — morphism sorts for each pair of objects

**Function symbols.**

- $\otimes \colon \mathrm{Ob} \times \mathrm{Ob} \to \mathrm{Ob}$
  (tensor product)
- $(-)^\vee \colon \mathrm{Ob} \to \mathrm{Ob}$ (rigid dual)
- $\mathbf{1} \colon \mathrm{Ob}$ (unit object, constant symbol)
- $\sigma_{X,Y} \colon \mathrm{Mor}(X \otimes Y,\; Y \otimes X)$
  (braiding)
- $\mathrm{ev}_X \colon \mathrm{Mor}(X^\vee \otimes X,\; \mathbf{1})$
  (evaluation)
- $\mathrm{coev}_X \colon \mathrm{Mor}(\mathbf{1},\; X \otimes X^\vee)$
  (coevaluation)

**Relation symbols.**

- $\cong$ (isomorphism of objects)
- $\hookrightarrow$ (subobject inclusion)

**Numeric term.**

- $\dim_q \colon \mathrm{Ob} \to \mathrm{End}(\mathbf{1})$, the
  quantum trace $\dim_q(X) = \mathrm{tr}_q(\mathrm{id}_X)$

**Axioms.** The rigid monoidal category axioms (associativity,
unit, evaluation/coevaluation zigzag identities) together with
the Hecke relation on the braiding:

$$(T - q)(T + q^{-1}) = 0$$

where $T = \sigma_{V,V}$ acts on $V \otimes V$ and
$q \in \mathrm{End}(\mathbf{1})$ is the substrate parameter.

The $q$-integers $[n]_q = (q^n - 1)/(q - 1)$ play the role of
**residues** in Pas's language of valued fields; the braiding
eigenvalues $q$ and $-q^{-1}$ play the role of **angular
components**. Tannaka–Krein reconstruction
($G_q \cong \mathrm{Aut}^\otimes(\tau)$) is the categorical analog
of **quantifier elimination**: every first-order sentence about
objects of $\mathbf{C}$ reduces to conditions on the fibre-functor
image $\tau(X)$ (underlying vector space = "residue data") together
with the $G_q$-action ("valuation data"), eliminating the categorical
quantifiers.
