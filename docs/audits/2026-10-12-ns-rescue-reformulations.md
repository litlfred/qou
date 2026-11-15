# Can any honest reformulation rescue an NS-singularity statement on Bring's surface?

**Date:** 2026-10-12. **Bean:** `qou-ocof` (owner-directed: *"keep exploring if a reformulation
could rescue"*). **Branch:** `ns-rescue`, based on `claude/bold-gates-00l1bl` at `4fd72a468`.
**Scope:** read-only audit. No content block, `.lean` file or witness was edited.

**Established inputs.** These are cited here and not re-derived:
- [`2026-10-12-ns-chain-after-item3-retraction.md`](2026-10-12-ns-chain-after-item3-retraction.md), "chain audit": $H^2(\Sigma,\cdot)=0$, $\delta_n=0$, the local-degree formula is wrong, and Kummer persistence is global.
- [`2026-10-12-jet-tower-band-construction.md`](2026-10-12-jet-tower-band-construction.md).
- [`2026-10-12-atiyah-jet-classes-bring.md`](2026-10-12-atiyah-jet-classes-bring.md).
- [`2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`](2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md), "cone-link audit". It shows that the link of Bring's cone is canonically $M:=UT(\Sigma_4)=\Gamma_4\backslash PSL(2,\mathbb R)$, with Euler number $-6$.

**Tags.** **[D]** derived here; **[S]** standard, cited; **[A]** asserted in the corpus without derivation; **[O]** open.

**Library.** I checked the index, `sections/` and `ocr/`.
- **Held:** `library/candetgl/` (Cantarella–DeTurck–Gluck, Biot–Savart operator). Its bibliography, `sec-025-acknowledgments.md:93`, cites Etnyre–Ghrist I, but the paper itself is not held. Also held: `library/helicity03mmj/` (higher helicities) and `library/procrsoclondona92/` (Moffatt–Ricca, helicity).
- **Not held:**
  - Etnyre–Ghrist, *Contact topology and hydrodynamics I* (Nonlinearity 13, 2000);
  - Arnold–Khesin, *Topological Methods in Hydrodynamics*;
  - Taubes, *The Seiberg–Witten equations and the Weinstein conjecture* (G&T 11, 2007);
  - Tao, *Finite time blowup for an averaged NS* (JAMS 2016);
  - Ladyzhenskaya and Wolibner, 2D regularity.
- **In `references.ts` but not in the library:** `cardona2021`, `cardona2023`, `tao2019`.

---

## 0. Verdict

**No honest reformulation among candidates 1–5 yields a true, non-vacuous statement that the topology forces a singularity of the model's NS flow.** Each candidate fails for a different reason:

| # | Candidate | Verdict | Decisive reason |
|---|---|---|---|
| 1 | The model's actual Reeb field vanishes on $\Sigma$ | **no**, scope (b) | The corpus defines the Reeb field as the generator of the free $U(1)$ fibre action. A Reeb field satisfies $\Theta(R)=1$, so it has no zeros anywhere. |
| 2 | $e(\xi)$ in $H^2_\Sigma(\mathcal S,\mathbb Z)$ | **partial: true but vacuous** | The image is $-6\cdot[\text{gen}]$, independent of the section. But it exists for every non-empty compact $\Sigma$, so it carries no information about collisions. |
| 3 | 3-manifold $M=UT(\Sigma_4)$ (Gysin, contact, Weinstein) | **no** for singularity; **open** only where every closed 3-manifold is open | $e(\ker\Theta)=0$ on $M$; the $-6$ survives only as $\mathbb Z/6$ torsion; the Reeb flow is periodic. |
| 4 | Hydrodynamic topology (Etnyre–Ghrist, Arnold, Tao, CMPP) | **no**; it points the **other way** | The model's Reeb field is a Beltrami field on $M$, which gives an explicit **globally smooth** NS solution (§4). |
| 5 | The Kummer class $-6\bmod n$ | **no**, scope (b) for "every solution" | It is a bundle invariant. The same bundle carries a regular solution. |

**Closest true statement found** (§7): $M=UT(\Sigma_4)$ carries an explicit eternal steady Euler flow and a globally smooth, exponentially decaying NS flow, both built from the model's own Reeb field. Topology therefore cannot force blow-up of all solutions. Whether some data on $M$ blows up is the 3D regularity problem on a closed 3-manifold. It is open on $M$, and it is equally open on $T^3=UT(T^2)$.

---

## 1. Two structural defects that every reformulation must face

**1a. The space $\mathcal S$ is used in two incompatible dimensions [D].**
- The tower and computation blocks use $\mathcal S$ as a closed Riemann surface. They rely on $H^2(\mathcal S,\mathcal O)=0$, $\chi=-6$ and $H^2(\mathcal S,\mathbb Z)\cong\mathbb Z$.
- `core-levi-form.md` uses $(\mathcal S,\varTheta)$ as a contact manifold with a Levi form on $\ker\varTheta$, carrying vortex filaments $\varrho$ and a normal plane $N_p\varrho\subset\ker\varTheta_p$.
- `q-metric-contact-deformation.md:13` writes "strict contact metric on $\mathcal S$".

A contact structure needs odd dimension at least 3. A filament with a 2-dimensional normal plane inside $\ker\varTheta$ needs dimension at least 3. So no single space can be both of these.

The only reconciliation the corpus itself supplies is the cone-link audit's $M=UT(\Sigma_4)\to\Sigma_4$. The surface carries $\chi$ and the Kummer data; $M$ carries $\Theta$, the Reeb field and the filaments. Every candidate below is therefore evaluated on whichever of the two spaces its object actually lives on. This is not a choice made to rescue anything: it is the only reading under which the blocks parse.

**1b. Internal sign conflict between the computation and the Levi chain [D].** The two halves of the chain take opposite branches:
- `ns-obstruction-computation.md` (c).1 says the topological term is non-zero **iff** the Reeb field vanishes at $p$ **iff** the contact structure degenerates.
- `ns-singularity-descartes-proof.md` Step 3 says $\mathrm{NS}(A)\neq0$ implies the contact structure **does not** degenerate.
- `levi-degeneracy-conjecture.md` (B) assigns contact degeneration to the **regular** branch.

So the mechanism that would make the topological term non-zero lands, by the corpus's own conjecture, in the NS-regular regime. Any rescue through "a Reeb zero on $\Sigma$" inherits this contradiction before topology even enters.

---

## 2. Candidate 1: does the model force its Reeb field to vanish on $\Sigma$?

**Object.** `mass-theory/reeb-bundle.md` defines $\xi_q$ as "the $q$-Reeb vector field generating the $U(1)$ fibre action" of a principal circle bundle. The cone-link audit identifies the circle bundle relevant to Bring as $M\to\Sigma_4$, Euler number $-6$. Its contact form is the restriction of the standard form on $S^9\subset\mathbb C^5$ to the link, which is a Boothby–Wang connection form [S]. The Reeb field is the fibre generator $V$.

**Fact [S].** A Reeb field satisfies $\Theta(R)\equiv1$, so it has no zeros. The generator of a free $S^1$-action also has no zeros. Where the contact form itself degenerates, $R$ is **undefined**, which is not the same as zero.

**What vanishes in the chain, then?** Only a section $s$ of the line bundle $T\Sigma_4$ on the surface (row 11 of the chain audit), for example the projection of some field to the base. Poincaré–Hopf forces $Z(s)\neq\varnothing$ with indices summing to $-6$. Isotopy moves any finite $Z(s)$ off $\Sigma$ [S]. The corpus defines no dynamics that pins $Z(s)$ to $\Sigma$:
- `ns-obstruction-computation.md:34` *asserts* that "at a vortex collision point the Reeb field forcibly zeroes out" [A]. The justification ("the contact structure must degenerate if the core flattens") is the regular branch by §1b.
- The $q$-NS system (`q-navier-stokes.md`) evolves $v\in\Omega^1(A)$; it never evolves the Reeb field.

**Verdict: no.**
- Scope **(b)** for "the model's Reeb field vanishes on $\Sigma$". The invariant is $\Theta(R)=1$, equivalently the freeness of the $U(1)$ action.
- Scope **(a)** for "some section of $T\Sigma_4$ selected by the flow vanishes on $\Sigma$". No such selection is defined. If one were defined, its zeros on $\Sigma$ would be a dynamical fact, not a topological one.

---

## 3. Candidate 2: relative classes $H^2_\Sigma(\mathcal S,\mathbb Z)=H^2(\mathcal S,\mathcal S\setminus\Sigma)$

**Correction to the bean's framing [D].** For a curve $\Sigma$ in a surface the codimension is **1**, not 2. The Thom isomorphism gives $H^k_\Sigma(\mathcal S)\cong H^{k-1}(\Sigma;o_\nu)$ for a closed two-sided curve, not $H^{k-2}$.

**The group [D].**
- *Arc (the corpus's "line segment").* Excision onto a disc neighbourhood $N$ gives $H^2_\Sigma\cong H^2(N,N\setminus\Sigma)\cong\tilde H^1(S^1)=\mathbb Z$.
- *Closed curve.* $H^2_\Sigma\cong H^1(S^1)=\mathbb Z$ (two-sided, since $\mathcal S$ is orientable).

**The map to $H^2(\mathcal S)$ [D].** In every case $H^2(\mathcal S\setminus\Sigma)=0$, because $\mathcal S\setminus\Sigma$ is a non-compact surface. So $H^2_\Sigma\to H^2(\mathcal S)$ is a surjection $\mathbb Z\to\mathbb Z$, hence an isomorphism. Exactness then forces the connecting map $\partial\colon H^1(\mathcal S\setminus\Sigma)\to H^2_\Sigma$ to be zero.

**Consequences.**
- $e(\xi)$ has a **unique** lift $-6\cdot[\text{gen}]\in H^2_\Sigma$.
- That lift is the relative Euler class of $(\xi,s)$ for **any** $s$ that is non-vanishing on $\mathcal S\setminus\Sigma$. Since $\partial=0$, it is independent of the choice of $s$.

So the image is non-zero and section-independent. Both properties the bean asked about hold.

**Why it is vacuous.** The identical statement holds for every non-empty compact $\Sigma'\subset\mathcal S$, including a single point far from any collision (the chain audit, §3.3). The true content is:

> *If a section of $T\Sigma_4$ is non-vanishing off a compact set $K$, then it has zeros in $K$ with indices summing to $-6$.*

That is Poincaré–Hopf with a support condition. It says nothing that singles out the collision locus. Its NS-relevant use would need the dynamical antecedent of candidate 1, which is not established.

**Verdict: partial.** True, section-independent and non-zero, but not specific to $\Sigma$. It cannot discriminate collision from non-collision, so it cannot carry an NS verdict.

---

## 4. Candidate 3: the 3-manifold $M=UT(\Sigma_4)$

**Cohomology [S] (Gysin).** $H_1(M;\mathbb Z)\cong\mathbb Z^{8}\oplus\mathbb Z/6$, and $H^2(M;\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/6$. The torsion is generated by $\pi^*[\Sigma_4]$, which is Poincaré dual to the fibre. The $-6$ survives on $M$ **only** as this torsion order. $\pi^*e(T\Sigma_4)=-6\,\pi^*[\Sigma_4]=0$.

**Contact plane field [S]/[D].**
- $M=\Gamma_4\backslash PSL(2,\mathbb R)$ carries the global left-invariant frame $(X,X^\perp,V)$: geodesic, normal, and fibre directions.
- The Boothby–Wang plane field $\ker V^\flat=\mathrm{span}(X,X^\perp)$ is therefore trivial, so $e(\ker\Theta)=0\in H^2(M)$.
- The geodesic-flow structure $\ker X^\flat$ is likewise trivial.

There is no non-zero Euler class of a plane field on $M$ for a section to "localise". The analogue of candidate 2 on $M$ is codimension 2: $H^2_\Sigma(M)\cong H^0(\Sigma)$ for a closed curve $\Sigma$. A torsion class localises on any fibre, which is again not specific to collisions.

**Tightness and Weinstein [S] (not held).**
- The Boothby–Wang structure on a negative-Euler circle bundle is the Milnor-fillable link structure. It is Stein-fillable, hence tight.
- Its Reeb flow is the fibre rotation: every orbit is periodic with a common period. The Weinstein conjecture (Taubes 2007) is satisfied trivially.
- These are theorems about a **steady** vector field: existence of closed orbits and fillability. They contain no time evolution and no blow-up criterion. Calling them a regularity statement would be analogy, not theorem.

**Levi form [S].** The link of an isolated surface singularity is strictly pseudoconvex. The Levi form of its canonical CR structure is definite at **every** point. Condition (3) of `core-levi-form` is therefore automatic for that structure, everywhere, independent of $\Sigma$. Whether the $q=1$ flow deforms the CR structure is not defined in the corpus [O].

**Verdict: no** for a topological singularity statement.

**The precise open question.** Does the 3D NS equation on $(M,g)$ for some smooth metric $g$ admit smooth divergence-free data that blows up in finite time? This is open on $M$ exactly as it is on $T^3$. Small data are globally regular on any closed Riemannian 3-manifold [S, Fujita–Kato type; not held].

This also exposes `torus-ns-regular.md`. Under the 3D reading its "$\chi=0$ forces regularity" is the periodic Clay problem on $T^3=UT(T^2)$, asserted without proof [A]. Under the 2D reading both genera are regular (§5), so the torus/Bring contrast discriminates nothing in either reading.

---

## 5. Candidate 4: hydrodynamic topology

**The model's Reeb field is a Beltrami field [D].** Equip $M$ with the left-invariant metric that makes $(X,X^\perp,V)$ orthonormal. The structure relations are those of $\mathfrak{psl}_2$ with $K=-1$; signs are up to orientation. Writing $\beta=V^\flat$:
1. $d\beta(X,X^\perp)=-\beta([X,X^\perp])=\mp1$, so $d\beta=\mp X^\flat\wedge X^{\perp\flat}$ and $\star d\beta=\mp\beta$. That is, $\mathrm{curl}\,V=\mp V$.
2. $V$ generates right multiplication by $SO(2)$. The metric is $\mathrm{Ad}(SO(2))$-invariant, so $V$ is Killing, hence divergence-free.
3. $i_V d\beta=0$, so $\nabla_VV=0$.

Hence:
- **Steady Euler [D].** $u\equiv V$ with constant pressure is a steady Euler solution, and it exists for all time.
- **Navier–Stokes [D].** With the Hodge Laplacian, $\Delta_H V=\mathrm{curl}^2V=V$. So $u(t)=e^{-\nu t}V$ is an exact solution of NS on $(M,g)$: the nonlinear term vanishes identically, as $\nabla_uu=0$.

The Bochner or deformation Laplacians differ by a Ricci term. By $\mathrm{Ad}(SO(2))$-invariance, $\mathrm{Ric}=a(X^\flat{}^2+X^{\perp\flat}{}^2)+b\,\beta^2$, so $\mathrm{Ric}(V)=bV$ and $V$ remains an eigenfield. Only the decay rate changes.

The data is smooth and the solution is smooth for $t\in[0,\infty)$. This is a construction on the model's own Reeb field and the model's own 3-manifold.

**Transfer of the literature** (all not held; `cardona*` and `tao2019` are in `references.ts`):
- **Etnyre–Ghrist.** Rotational Beltrami fields are Reeb fields up to rescaling, and vice versa. This transfers exactly: the identification above is an instance. It concerns *steady inviscid* flows, which do not blow up.
- **Arnold (helicity).** $\mathcal H(V)=\int\langle V,\mathrm{curl}\,V\rangle=\mp\mathrm{vol}(M)\neq0$. Non-zero helicity bounds the energy from below along *Euler* volume-preserving rearrangements. It is not conserved by NS, and it gives no blow-up.
- **CMPP (`cardona2021`, `cardona2023`).** Turing-complete steady Euler flows, via Reeb fields of specially constructed contact forms and metrics on $S^3$ and $\mathbb R^3$. That yields *undecidability* of orbit questions for a steady flow. It is not a singularity. It also does not apply to the model's fixed Boothby–Wang/geodesic structure, whose Reeb flow is periodic.

  `q-metric-contact-deformation.md:13` ("Reeb flow Turing-complete" for generic $q>1$) is therefore [A]: no construction is given for this $M$ and this form.
- **Tao (`tao2019`; JAMS 2016 not held).**
  - The 2019 universality result embeds dynamics into Euler flows on *some* manifold with a *chosen* metric. The manifold and metric are outputs, not a given $UT(\Sigma_4)$.
  - The 2016 blow-up is for an *averaged* nonlinearity on $\mathbb R^3$, not for NS.
  - Neither transfers to a singularity statement about the model.
- **2D (on the surface itself) [S, not held].** Ladyzhenskaya and Wolibner/Kato: smooth solutions of NS and of Euler on a closed Riemannian 2-manifold are global. Any reading that places the flow on $\Sigma_4$ itself is **excluded** from singularity, scope (b), with that theorem as the invariant.

**Verdict: no rescue.** The only exact transfer, Etnyre–Ghrist, produces a **globally regular** NS solution from the model's Reeb field.

---

## 6. Candidate 5: Kummer and arithmetic, $-6\bmod n$

The class $\partial_n[\xi]=-6\bmod n\in H^2(\Sigma_4,\mu_n)$ (chain audit §2) is an invariant of the circle bundle. On $M$ it is the statement that the fibre, i.e. the Reeb orbit, has order exactly 6 in $H_1(M;\mathbb Z)$ [D, from §4]. That is a true dynamical-topological fact: **every Reeb orbit is a 6-torsion homology class**.

It is invariant under every diffeomorphism and every smooth time evolution, and it is shared by the regular solution of §5. So it cannot force *every* solution to be singular. That is scope (b), with the invariant being the explicit regular solution on the same bundle. It also gives no mechanism toward *some* solution being singular, scope (a).

**Verdict: no.**

---

## 7. Closest true statements, and what would change the verdict

**True and non-vacuous [D/S]:**
1. $e(T\Sigma_4)=-6$; $T\Sigma_4$ has an $n$-th root iff $n\mid6$ (chain audit).
2. On $M=UT(\Sigma_4)$:
   - the $-6$ is the order of the Reeb-orbit class in $H_1(M)$;
   - the contact plane field is trivial and tight;
   - the Reeb field has no zeros and is periodic.
3. The model's Reeb field $V$ is a Beltrami field for the left-invariant metric. It is an eternal steady Euler flow, and $e^{-\nu t}V$ is a globally smooth NS solution on $M$.
4. NS and Euler on the surface $\Sigma_4$ are globally regular.

Statements 3 and 4 relate the model's topology to its flow **in the regularity direction**.

**What would reopen a singularity reading** (each [O], and none is topological):
- (i) A definition in the corpus of the time-dependent $q=1$ flow **on $M$** together with its initial data, followed by a proof that that particular data blows up. This is the Clay problem on $M$.
- (ii) A dynamical theorem pinning a flow-selected section's zeros to a flow-defined $\Sigma$. Even then, §1b's sign conflict must be resolved first.

---

## 8. Recommendation (judgement, not finding)

1. **Record the negative.** Close the search for a *topological* NS-singularity criterion on Bring as "no honest rescue in candidates 1–5". Keep `thm:ns-singularity-descartes` restated as topological facts (option B), as the chain audit recommends.
2. **Owner decision: optionally add statement 3 of §7 as a new proposition.** It is short, falsifiable, and derived from the model's own Reeb field.
   - *Cost:* one block plus a Lean scaffold.
   - *Risk:* it says the model's natural flow is regular, which runs against the current narrative.
   - *Default if the owner does nothing:* nothing changes.
3. **The two defects of §1 are independent of this bean.** $\mathcal S$ is used in two dimensions, and the computation and the Levi chain take opposite branches. Both make the chain incoherent before any rescue. They should be scoped in the blocks that carry them, as a separate, owner-approved edit.
4. **Do not pursue** Turing-completeness or the Weinstein conjecture as a route. Both concern steady flows, and neither is constructed for this structure.
