### Proof

**Step 1.** We apply [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin). Over any number field $F$, the depth-2 grouplike image $\tau_{\mathrm{arch}}(G^{(2)}|_F) / \mathcal{P}_1$ is isomorphic to $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$ via the Bloch–Suslin regulator. This requires no conditional assumptions.

**Step 2.** We set $F = \mathbb{Q}(\zeta_6) = \mathbb{Q}(\sqrt{-3})$. Borel's theorem yields $\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(\zeta_6)) \otimes \mathbb{Q} = 1$ ([`prop:borel-partial-resolution`](#prop:borel-partial-resolution)). The Bloch–Suslin regulator's image is the $\mathbb{Q}$-line spanned by $D(\zeta_6) = \mathrm{Cl}_2(\pi/3)$.

**Step 3.** We pair $e_{(2,2)} \in Z(H_4(q))$ with $\mathrm{Li}_2^q(\zeta_6) \in G^{(2)}(\mathcal{H}_q)$ via the Markov trace. This explicit Hoefsmit/Markov computation yields the specific number $2 D(\zeta_6) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.029\ldots$. This matches the 50-digit numerical verification in [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).

**Step 4.** We apply Murakami–Murakami (2001) [@murakami-murakami2001]:

$$
  \lim_{N \to \infty} \frac{2\pi}{N} \log\!\bigl|J_{4_1}^{(N)}(e^{2\pi i/N})\bigr|
  \;=\;
  \mathrm{Vol}(S^3 \setminus 4_1)
  \;=\;
  2\,\mathrm{Cl}_2(\pi/3).
$$

They establish this asymptotic via a Faddeev–Kashaev quantum-dilogarithm expansion and saddle-point analysis.

**Step 5.** Steps 1–3 give $\tau_{\mathrm{arch}}(e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6)) = 2\,\mathrm{Cl}_2(\pi/3)$. This matches the Bloch–Suslin regulator image. Step 4 confirms this is exactly $\mathrm{Vol}(4_1)$, which is the geometric invariant predicted by the Volume Conjecture. Thus, we discharge B1 at this row:

- We obtain a depth match by construction. $\mathrm{Li}_2^q$ appears at depth 2, and $\mathrm{Vol}(4_1)$ appears at Goncharov depth 2.
- We obtain a numerical match from Step 3 and Step 4.
- We obtain inclusion from Step 1.
- We obtain strong sharpness from Step 2. The Borel rank is 1, which exactly matches the line spanned by $\mathrm{Vol}(4_1)$.

$\square$
