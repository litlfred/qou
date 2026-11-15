---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-010-generating-two-additional-generations-from-s3-au
section_title: "Generating two additional generations from S3 automorphisms"
section_number: null
pages: 11-13
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.975
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
---
Having constructed one generation of electrocolor states, we now proceed to apply $\psi$ to the ladder operators eqns. ([\[newladder1\]](#newladder1){reference-type="ref" reference="newladder1"})-([\[newladder3\]](#newladder3){reference-type="ref" reference="newladder3"}), and subsequently the basis states of the minimal left ideals, in order to generate two additional generations.

The first thing to check is that the $S_3$ automorphisms of $\mathbb{S}$ carry over the automorphisms of the left multiplication algebra $\mathbb{C}\ell(8)$. Given the generating basis $e_0,...,e_8$ for $\mathbb{C}\ell(8)$, it is readily verified that $$\begin{aligned}
    \psi(e_i)\psi(e_i)=\psi(e_i^2)=-1,\\
    \psi(e_i)\psi(e_j)+\psi(e_i)\psi(e_j)=0.
\end{aligned}$$ Subsequently, $\psi$ extends to an automorphism of the entire $\mathbb{C}\ell(8)$ algebra (see Lemma 9.7 of [@harvey1990spinors]). A similar argument holds for the order two $S_3$ automorphism $\epsilon$ of $\mathbb{S}$, which likewise extends to an automorphism of $\mathbb{C}\ell(8)$. It can furthermore be checked that: $$\begin{aligned}
    \psi(e_{i+8})\psi(e_{i+8})=\psi(e_{i+8}^2)=-1,\\
    \psi(e_{i+8})\psi(e_{j+8})=-\psi(e_{i+8})\psi(e_{j+8}).
\end{aligned}$$ Finally, one also find that $$\begin{aligned}
    \psi^2(e_i)+\psi(e_i)+e_i=0,\\
    \psi^2(e_{i+8})+\psi(e_{i+8})+e_{i+8}=0,
\end{aligned}$$ indicating that $\psi^2(e_i),\; \psi(e_i)$ and $e_i$ (as well as $\psi^2(e_{i+8}),\; \psi(e_{i+8})$ and $e_{i+8}$) are not linearly independent. These conditions however are not satisfied by more general $\mathbb{C}\ell(8)$ multivectors (nor for $e_8$, which is fixed by $\psi$).

Since the action of $\psi$ on $e_1,...,e_{15}$ as elements of $\mathbb{C}\ell(8)$ is known, we can via linearity establish the action of $\psi$ on the ladder operators. This gives the three sets of ladder operators: $$\begin{aligned}
    A_i^{\dagger}&=&\frac{1}{2\sqrt{2}}(e_i+ie_{i+4}+e_{i+8}+ie_{i+12}),\\
    A_i&=&\frac{1}{2\sqrt{2}}(-e_i+ie_{i+4}-e_{i+8}+ie_{i+12}),\\
    \psi(A_i^{\dagger})=B_i^{\dagger}&=&\frac{1}{2\sqrt{2}}(ae_i+iae_{i+4}+be_{i+8}+ibe_{i+12}),\\
    \psi(A_i)=B_i&=&\frac{1}{2\sqrt{2}}(-ae_i+iae_{i+4}-be_{i+8}+ibe_{i+12}),\\
    \psi^2(A_i^{\dagger})=C_i^{\dagger}&=&\frac{1}{2\sqrt{2}}(be_i+ibe_{i+4}+ae_{i+8}+iae_{i+12}),\\
    \psi^2(A_i)=C_i&=&\frac{1}{2\sqrt{2}}(-be_i+ibe_{i+4}-ae_{i+8}+iae_{i+12}),
\end{aligned}$$ where $i=1,2,3$, and $$\begin{aligned}
    a=\frac{\sqrt{3}-1}{2},\qquad b=\frac{-\sqrt{3}-1}{2},
\end{aligned}$$ satisfying $a^2+b^2=2,\; a+b=-1,\; ab=-1/2$.

The three sets of ladder operators are not linearly independent since $$\begin{aligned}
\label{conditionladder}
    \psi^2(A_i^{\dagger})+\psi(A_i^{\dagger})+A_i^{\dagger}=0.
\end{aligned}$$

The two additional sets of ladder operators $\{B_i^{\dagger},B_i\}$ and $\{C^{\dagger},C_i\}$ generated in this manner likewise constitute Witt bases for $\mathbb{C}\ell(6)$, satisfying the same anticommutation relations as $\{A_i^{\dagger},A_i\}$, and we proceed to construct an additional pair of minimal left ideals of $\mathbb{C}\ell(6)$ for each of the two additional sets of ladder operators $\{B_iB_i^{\dagger}\}$ and $\{C_i,C_i^{\dagger}\}$. We interpret these additional pairs of minimal ideals as representing the second and third generation of electrocolor states: $$\notag
 \begin{split}
     S_2^u=&{\nu_{\mu}}\omega_2\omega_2^\dagger + \\  \overline{c^r}{B_1^\dagger}\omega_2\omega_2^\dagger + &\overline{c^g}{B_2^\dagger}\omega_2\omega_2^\dagger + \overline{c^b}{B_3^\dagger}\omega_2\omega_2^\dagger + \\ s^r{B_3^\dagger}{B_2^\dagger}\omega_2\omega_2^\dagger + &s^g{B_1^\dagger}{B_3^\dagger}\omega_2\omega_2^\dagger + s^b{B_2^\dagger}{B_1^\dagger}\omega_2\omega_2^\dagger + \\ &\mu^+{B_3^\dagger}{B_2^\dagger}{B_1^\dagger}\omega_2\omega_2^\dagger
\end{split}
\qquad 
\begin{split}
     S_2^d=&{\overline{\nu}_{\mu}}\omega_2^\dagger\omega_2 + \\ {c}^r{B_1}\omega_2^\dagger\omega_2 + &{c}^g{B_2}\omega_2^\dagger\omega_2 +  {c}^b{B_3}\omega_2^\dagger\omega_2 + \\ \overline{s^r}{B_3}{B_2}\omega_2^\dagger\omega_2 + &\overline{s^g}{B_1}{B_3}\omega_2^\dagger\omega_2 + \overline{s^b}{B_2}{B_1}\omega_2^\dagger\omega_2 + \\ &\mu^-{B_3}{B_2}{B_1}\omega_2^\dagger\omega_2
\end{split}$$

$$\notag
 \begin{split}
     S_3^u=&{\nu_{\tau}}\omega_3\omega_3^\dagger + \\  \overline{b^r}{C_1^\dagger}\omega_3\omega_3^\dagger + &\overline{b^g}{C_2^\dagger}\omega_3\omega_3^\dagger + \overline{b^b}{C_3^\dagger}\omega_3\omega_3^\dagger + \\ t^r{C_3^\dagger}{C_2^\dagger}\omega_3\omega_3^\dagger + &t^g{C_1^\dagger}{C_3^\dagger}\omega_3\omega_3^\dagger + t^b{C_2^\dagger}{C_1^\dagger}\omega_3\omega_3^\dagger + \\ &\tau^+{C_3^\dagger}{C_2^\dagger}{C_1^\dagger}\omega_3\omega_3^\dagger
\end{split}
\qquad 
\begin{split}
     S_3^d=&{\overline{\nu}_{\tau}}\omega_3^\dagger\omega_3 + \\ {b}^r{C_1}\omega_3^\dagger\omega_3 + &{b}^g{C_2}\omega_3^\dagger\omega_3 +  {b}^b{C_3}\omega_3^\dagger\omega_3 + \\ \overline{t^r}{C_3}{C_2}\omega_3^\dagger\omega_3 + &\overline{t^g}{C_1}{C_3}\omega_3^\dagger\omega_3 + \overline{t^b}{C_2}{C_1}\omega_3^\dagger\omega_3 + \\ &\tau^-{C_3}{C_2}{C_1}\omega_3^\dagger\omega_3
\end{split}$$ Here, $\omega_2:=B_1B_2B_3,\;\omega_3:=C_1C_2C_3$.

That is the order three automorphism $\psi$ of the finite group $S_3$ can be used to construct exactly two additional generations of color states. This automorphism then permutes between the three generations.

On the other hand, the order two automorphism $\epsilon$ does not generate transformations between the three generations. Applying $\epsilon$ to the ladder operators $A_i$ and $A_i^{\dagger}$ generates an complementary set of ladder operators satisfying the same anticommutation relations as $A_i$ and $A_i^{\dagger}$ (since $\epsilon$ is an automorphism of $\mathbb{C}\ell(8)$), and hence can likewise be used to construct minimal ideals. The automorphism $\epsilon$ can then be used to incorporate an additional degree of freedom (perhaps chirality, handedness, or spin). It is not immediately clear at present however what the most natural physical interpretation for $\epsilon$ is.
