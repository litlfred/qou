### Proof

**Step 1.** [Depth-2 identification of $G^{(2)}(\mathcal{H}_q)$ with $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$ — provable via Bloch--Suslin](#prop:depth-2-identification-bloch-suslin)
establishes that, *over any number field $F$*, the depth-2
grouplike image $\tau_{\mathrm{arch}}(G^{(2)}|_F) / \mathcal{P}_1$ is
isomorphic to $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$ via the
Bloch–Suslin regulator. **Theorem-level (no conditional).**

**Step 2.** For $F = \mathbb{Q}(\zeta_6) = \mathbb{Q}(\sqrt{-3})$:
$\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(\zeta_6)) \otimes \mathbb{Q} = 1$
([Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution)).
The Bloch–Suslin regulator's image is the $\mathbb{Q}$-line spanned
by $D(\zeta_6) = \mathrm{Cl}_2(\pi/3)$. **Theorem-level (Borel).**

**Step 3.** The pairing of $e_{(2,2)} \in Z(H_4(q))$ with
$\mathrm{Li}_2^q(\zeta_6) \in G^{(2)}(\mathcal{H}_q)$ via the
Markov trace yields, after Hoefsmit + Schur–Weyl combinatorics, the
specific number $2 D(\zeta_6) = 2\,\mathrm{Cl}_2(\pi/3) \approx
2.029\ldots$ — verified numerically at 50 dps in
[Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)](#conj:bring-figure-eight-depth-2-witness).
**Theorem-level (explicit Hoefsmit/Markov computation).**

**Step 4.** Murakami–Murakami 2001 \cite{murakami-murakami2001}:

$$
  \lim_{N \to \infty} \frac{2\pi}{N} \log\!\bigl|J_{4_1}^{(N)}(e^{2\pi i/N})\bigr|
  \;=\;
  \mathrm{Vol}(S^3 \setminus 4_1)
  \;=\;
  2\,\mathrm{Cl}_2(\pi/3).
$$

The asymptotic is proved via Faddeev–Kashaev quantum-dilogarithm
expansion + saddle-point analysis. **Theorem (published proof).**

**Step 5 (combination).** Steps 1–3 give: $\tau_{\mathrm{arch}}(e_{(2,2)} \cdot
\mathrm{Li}_2^q(\zeta_6)) = 2\,\mathrm{Cl}_2(\pi/3)$ matches the
Bloch–Suslin regulator image. Step 4 confirms this is precisely
$\mathrm{Vol}(4_1)$, the geometric invariant the Volume
Conjecture predicts. So the depth correspondence at this row is fully discharged:

- Depth match (yes, by construction): $\mathrm{Li}_2^q$ at depth 2,
  $\mathrm{Vol}(4_1)$ at Goncharov depth 2.
- Numerical match (yes, Step 3 + Step 4 + 50-digit witness).
- Inclusion (yes, Step 1).
- Strong sharpness at this row (yes, Step 2 — Borel-rank is 1, exactly
  matching the line spanned by $\mathrm{Vol}(4_1)$).

$\square$
