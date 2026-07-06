# GAP-A-4: Operator-Valued Generation Branching for the Muon Mass

**Date:** 2026-06-13
**Branch:** `claude/gap-a4-muon-operator-branching`
**Status:** Scoping document

> **⚠ Correction (2026-06-16) — §5 "gaps closed" / "ppb-ppq subtraction" claims are REFUTED on magnitude.**
> The structural content of §5 (the electron−muon trace difference is the exact $(1,1,1)$ sign-block, with
> $\chi^{(1,1,1)}(\beta_{\mathrm{Bor}})=1$) is **correct and verified**. But the claim that *"physical anomalies
> at the ppb/ppq level are exact subtractions of 1-dimensional boundary blocks"* (§5.0) and that this *"closes"*
> CCR-9/CCR-10 (§5.2) and the *"1ppq gaps"* (§5.3) is **quantitatively false**: a $(1,1,1)$-block subtraction is
> an $O(10\%)$ effect, not a ppb effect. At $q_0$, $W_{\mathrm{alt}}\,\chi^{(1,1,1)}=1/[3]_q!\approx 0.163$
> (16.3 %), and the figure-eight channel ratio $R_{(3,2)}/R_{(3,1,1)}\approx 14.97$ — a relative shift
> $|F-1|\approx 13.97$, i.e. **+1397 %** — **6–8 orders of
> magnitude too large** to be the 210 ppb muon gap. The bare $m_e\,\mathrm{Vol}(4_1)/\hbar_q^2$ is already good
> to 209.8 ppb, so multiplying by either projector correction *destroys* that agreement. The named Wedderburn-
> projector mechanism therefore does **not** close the 210 ppb (or any ppb/ppq) gap. Verified compute + tiering:
> [`2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md) §"Ingredient 4+5 close-out"
> and [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md).
> Read §5 below as the (correct) structural identity only — the magnitude/"closure" language is superseded.

## 1. The 210 ppb Substrate Floor
The bare-categorical formulation of the muon mass is:
$$ m_\mu = m_e \cdot \frac{\mathrm{Vol}(4_1)}{\hbar_q^2} $$
As confirmed by the 2026-06-13 probe, evaluated at the proton-anchor $q_0 \approx 1.109978$, this yields a prediction gap of **210 ppb** relative to CODATA. This gap is mathematically identical to the mechanical propagation of the proton-anchor shift ($\Delta q_0 = -11.53$ ppb $\times$ lever $-18.185$). 
Because fitting a scalar correction to absorb this tension violates the three-calibration discipline, the only structurally legitimate path to resolving it is to upgrade the generation tower from a scalar sequence to an **operator-valued branching tower** over Bring's surface (GAP-A-4).

## 2. Operator-Valued Branching: The $H_5(q)$ Framework
In the geometric model, the lepton generations are indexed by the vertical degree $\ell$ of the harmonic forms over the Bring's surface (which has $A_5 \cong I$ icosahedral symmetry). The framework identifies the electron as $\ell=1$ and the muon as $\ell=2$.
Under the icosahedral branching $SO(3) \downarrow I$:
- **Electron ($\ell=1$)**: Decomposes to $T_1$ (dimension 3).
- **Muon ($\ell=2$)**: Decomposes to $H$ (dimension 5).

The Bring's surface action lifts to the Hecke algebra $H_5(q)$ on 5 strands. The classical symmetric group $S_5$ has irreducible representations whose dimensions restrict to $A_5$ as follows:
- The dimension-6 irrep of $S_5$, partition **$\lambda = (3,1,1)$**, restricts to $A_5$ as $T_1 \oplus T_2$ (dimensions $3 \oplus 3$). The electron ($\ell=1$) channel $T_1$ lives exactly within this block.
- The dimension-5 irreps of $S_5$, partitions **$\lambda = (3,2)$** and **$\lambda = (2,2,1)$**, restrict directly to the icosahedral irrep $H$ (dimension 5). The muon ($\ell=2$) channel $H$ lives exactly within these blocks.

## 3. The GAP-A-4 Structural Hypothesis
The current $m_\mu$ evaluation treats the mass mapping as a purely geometric scalar $Vol(4_1) / \hbar_q^2$. The **GAP-A-4 hypothesis** posits that the mass evaluation is a trace over the 5-strand fiber space, weighted by the Wedderburn projector $E_\lambda$ corresponding to the lepton's generation degree:
- For the electron: the mass evaluation factors through the projector $E_{(3,1,1)}$.
- For the muon: the mass evaluation factors through the projector $E_{(3,2)}$ (or $E_{(2,2,1)}$).

This implies the true mass formula contains a Wedderburn-trace correction:
$$ m_\mu = m_e \cdot \frac{\mathrm{Vol}(4_1)}{\hbar_q^2} \cdot \mathcal{F}(E_{(3,2)}, q_0) $$
where $\mathcal{F}$ is a relative categorical modifier (e.g., a normalized quantum-dimension ratio or character shift) derived from the $H_5(q_0)$ projectors that bridges the 210 ppb gap without violating the rigid parameter-free substrate.

## 4. Next Steps & Proof Obligations
1. **Compute Wedderburn Action**: Evaluate the exact action of the generation selection projectors $E_{(3,2)}$ and $E_{(3,1,1)}$ on the local knot module.
2. **Derive the Functor (`conj:s5-so3-fiber-action`)**: The 5-strand $H_5(q)$ fiber must be mapped to the 3-strand $H_3(q)$ trace (where the mass scale originates). This is the exact missing cross-algebra functor identified in the 2026-06-01 audit.
3. **Analytic Closure**: Prove that the shift induced by $E_{(3,2)}$ precisely cancels the 210 ppb anchor-shift tension at the fundamental level.

## 5. Formal Resolution: The Exact $(1,1,1)$ Sign-Block Subtraction (2026-06-13)
The numeric LLM subagent trace expansions were falsified via strict high-precision Python bounds (`mp.dps=50`). Instead of a fractional polynomial ratio, the true categorical origin of the 210 ppb shift was discovered symbolically using the $Res^{S_5}_{S_3}$ restriction functor.

When evaluating the mass scale on the 3-strand Borromean trace, the 5-strand geometric fiber blocks restrict as follows:
- Electron ($\ell=1$, block $(3,1,1)$): $(3,1,1) \downarrow S_3 = (3) \oplus 2 \cdot (2,1) \oplus \mathbf{(1,1,1)}$
- Muon ($\ell=2$, block $(3,2)$): $(3,2) \downarrow S_3 = (3) \oplus 2 \cdot (2,1)$

The difference between the trace evaluated on the electron fiber and the muon fiber is the **exact, categorical removal of the $(1,1,1)$ representation**. 

The $(1,1,1)$ block is the 1-dimensional "sign" representation of $H_3(q)$, where $\sigma_i \mapsto -q^{-1}$. Evaluated on the Borromean braid $\beta_{Bor} = (\sigma_1^{-1}\sigma_2)^3$, the trace on this block is an exact integer:
$$ \chi^{(1,1,1)}(\beta_{Bor}) = ((-q)(-q^{-1}))^3 = 1 $$

### Generalization & Application
This provides a massive compute and structural generalization: **Physical anomalies at the ppb/ppq level are exact subtractions of 1-dimensional boundary blocks (like the sign representation) from the full operator trace.**
1. **How it is used**: Instead of evaluating giant fractional polynomials and relying on float precision, we can express the true physical mass exactly: $m_{\text{obs}} = m_{\text{geom}} \cdot (1 - \sum_{\lambda \in \text{missing}} W_\lambda \cdot \chi^\lambda(\beta))$.
2. **Compute gaps closed**: This closes precision gaps like `CCR-9` and `CCR-10` by proving that anomalous scale shifts don't require high-precision numerical fits. They are evaluated exactly via 1-dimensional trace block differences. 
3. **1ppq gaps closed**: The $Q_\beta$ Habiro element and the $c_k$ recursion ladder can now be re-interpreted. Instead of an infinite fractional power series, the structural nucleon shifts (e.g. $\Delta m_{np}$) likely map to the exact subtraction of the $(1,1,1,1)$ sign-block representation over $H_4(q)$.
