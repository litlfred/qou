---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-008-why-not-sedenions
section_title: "Why not sedenions?"
section_number: null
pages: 9-10
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.768
latex_coverage_ratio: 1.0
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
---
Since one generation of electrocolor states are efficiently represented starting from $\mathbb{C}\otimes\mathbb{O}$, one might ask if $\mathbb{S}$ (or rather $\mathbb{C}\otimes\mathbb{S}$) is an appropriate larger algebraic structure capable of describing three generations. Not being a division algebra is not grounds to disqualify $\mathbb{S}$, for we point out that neither $\mathbb{C}\otimes\mathbb{O}$ nor $\mathbb{C}\ell(6)$ generated as the left multiplication algebra are themselves division algebras. Furthermore, the algebra $\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$ is, like $\mathbb{S}$, not even alternative. in fact, the construction of invariant subspaces (minimal ideals) relies explicitly on the use of projectors (and nilpotents), which altogether do not exist in division algebras.

There are several natural reasons to suspect that $\mathbb{S}$ exhibits the algebraic structure necessary to describe three full generations:

1.  $Aut(\mathbb{S})=Aut(\mathbb{O})\times S_3$, and one finds a threefold multiplicity of the symmetries associated with $\mathbb{O}$,

2.  The process in Section [\[sedenions\]](#sedenions){reference-type="ref" reference="sedenions"} shows how to naturally isolate thee $\mathbb{O}$ subalgebras within $\mathbb{S}$, which could perhaps be used to construct three generations,

3.  The group $Spin(8)$ generated from $\mathbb{C}\ell(8)$ admits a triality, which has on occasion been suggested as a potential source of three generations [@boyle2020standard2; @masi2021exceptional]. The group of outer-automorphisms of $Spin(8)$ is precisely $S_3$.

One approach to construct three generations with $SU(3)_C$ symmetry is to use each of the three $\mathbb{C}\otimes\mathbb{O}_i\subset \mathbb{S}$ to generate (via its left action on itself, but not as a left action of $\mathbb{C}\otimes\mathbb{S}$!) a $\mathbb{C}\ell(6)$ algebra, and subsequently representing three generations in terms of the minimal left ideals of these three $\mathbb{C}\ell(6)$. This approach was considered in [@gillard2019three], as a generalization of the construction of three generations of leptons from three $\mathbb{H}\subset \mathbb{O}$ developed in [@manogue1999dimensional].

There are several drawbacks to this approach however. Each generation requires its own copy of $SU(3)$ resulting in three generations of gluons. Finally, the physical interpretation of the $S_3$ automorphisms remains obscured, because these automorphisms stabilize the (non-principle) octonion subalgebras in $\mathbb{S}$.

The approach pursued here is different and seeks to resolve these shortcomings. We instead use each $\mathbb{C}\otimes\mathbb{O}_i\subset \mathbb{S}$ to construct a pair or fermionic ladder operators that each generate $\mathbb{C}\ell(2)$, via their left multiplication action on all of $\mathbb{C}\otimes\mathbb{S}$ (instead of just $\mathbb{C}\otimes\mathbb{O}_i$). The three pairs of ladder operators are independent of one another and hence we identify a single copy of $\mathbb{C}\ell(6)\cong\mathbb{C}\ell(2)\hat{\otimes}\mathbb{C}\ell(2)\hat{\otimes}\mathbb{C}\ell(2)$, corresponding to a subalgebra of $\mathbb{C}\ell(8)$. Thus, we will employ all three $\mathbb{O}_i\subset \mathbb{S}$ in order to construct a single generation of states. This corresponds to a direct generalization of the construction of reviewed in Section [\[Furey\]](#Furey){reference-type="ref" reference="Furey"} where three $\mathbb{H}$ subalgebras of $\mathbb{O}$ are used to construct a single generation of color states. Subsequently, the order three $S_3$ automorphism of $\mathbb{S}$ will be used to generate two additional generations. This construction will therefore provide a clear interpretation of the new $S_3$ automorphism $\psi$. All three generations constructed in this manner transform as required under a single copy of the gauge group $SU(3)_C$, thereby avoiding introducing three generations of gluons.

## One generation of electrocolor states from $\mathbb{C}\otimes\mathbb{S}$ {#onegenS}

We proceed by first constructing a single generation with unbroken $SU(3)_C\times U(1)$ symmetry from $\mathbb{C}\otimes\mathbb{S}$. Considering the three octonion subalgebras $\mathbb{O}_1,\mathbb{O}_2,\mathbb{O}_3$ of $\mathbb{S}$ defined above: $$\begin{aligned}
\mathbb{O}_1&:& \{e_0,e_1,e_4,e_5,e_8,e_9,e_{12},e_{13}\}\\
\mathbb{O}_2&:& \{e_0,e_2,e_4,e_6,e_8,e_{10},e_{12},e_{14}\}\\
\mathbb{O}_3&:& \{e_0,e_3,e_4,e_7,e_8,e_{11},e_{12},e_{15}\}.
\end{aligned}$$

For each $\mathbb{O}_i$ subalgebra, we define a single pair of raising and lowering operators as follows: $$\begin{aligned}
\label{newladder1} A_1^{\dagger}&\equiv&\frac{1}{2\sqrt{2}}(e_1+ie_5+e_9+ie_{13}),\quad A_1\equiv \frac{1}{2\sqrt{2}}(-e_1+ie_5-e_9+ie_{13})\\
\label{newladder2} A_2^{\dagger}&\equiv& \frac{1}{2\sqrt{2}}(e_2+ie_6+e_{10}+ie_{14}),\quad A_2\equiv \frac{1}{2\sqrt{2}}(-e_2+ie_6-e_{10}+ie_{14})\\
\label{newladder3} A_3^{\dagger}&\equiv&\frac{1}{2\sqrt{2}}(e_3+ie_7+e_{11}+ie_{15}),\quad A_3\equiv \frac{1}{2\sqrt{2}}(-e_3+ie_7-e_{11}+ie_{15}).
\end{aligned}$$ It is readily checked that $A_i(A_iw)=A_i^{\dagger}(A_i^{\dagger}w)=0$ and $A_i(A_jw)=-A_j(A_iw)$, $\forall w\in \mathbb{C}\otimes\mathbb{S}$, and therefore these ladder operators satisfy (as left actions on a general $w\in\mathbb{S}$) the usual anticommutation relations: $$\begin{aligned}
    \{A_i,A_j\}w=\{A_i^{\dagger},A_j^{\dagger}\}w=0,\quad \{A_i,A_j^{\dagger}\}w=\delta_{ij}w,\; \forall w\in \mathbb{C}\otimes\mathbb{S}.
\end{aligned}$$ Each $A_i\in \mathbb{O}_i\subset \mathbb{S}$ in a generalization of $\alpha_i\in\mathbb{H}_i\subset \mathbb{O}$ where now each ladder operators consists of four terms instead of just two.

Subsequently we can proceed to construct two minimal left ideals, in a manner identical as in Section [\[Furey\]](#Furey){reference-type="ref" reference="Furey"}. These ideals are identical to $S^u$ and $S^d$ above, and (as will be demonstrated shortly) preserved by the same unitary symmetries, but with both the states and symmetry generators written in terms of the generalised ladder operators $A_i$ and $A_i^{\dagger}$.

$$\notag
 \begin{split}
     S_1^u=&{\nu_{e}}\omega_1\omega_1^\dagger + \\  \overline{d^r}{A_1^\dagger}\omega_1\omega_1^\dagger + &\overline{d^g}{A_2^\dagger}\omega_1\omega_1^\dagger + \overline{d^b}{A_3^\dagger}\omega_1\omega_1^\dagger + \\ u^r{A_3^\dagger}{A_2^\dagger}\omega_1\omega_1^\dagger + &u^g{A_1^\dagger}{A_3^\dagger}\omega_1\omega_1^\dagger + u^b{A_2^\dagger}{A_1^\dagger}\omega_1\omega_1^\dagger + \\ &e^+{A_3^\dagger}{A_2^\dagger}{A_1^\dagger}\omega_1\omega_1^\dagger,
\end{split}
\qquad 
\begin{split}
     S_1^d=&{\overline{\nu}_{e}}\omega_1^\dagger\omega_1 + \\ {d}^r{A_1}\omega_1^\dagger\omega_1 + &{d}^g{A_2}\omega_1^\dagger\omega_1 +  {d}^b{A_3}\omega_1^\dagger\omega_1 + \\ \overline{u^r}{A_3}{A_2}\omega_1^\dagger\omega_1 + &\overline{u^g}{A_1}{A_3}\omega_1^\dagger\omega_1 + \overline{u^b}{A_2}{A_1}\omega_1^\dagger\omega_1 + \\ &e^-{A_3}{A_2}{A_1}\omega_1^\dagger\omega_1,
\end{split}$$ where $\omega_1:=A_1A_2A_3$.

The $SU(3)_C$ generators are now a direct generalization of those in Section [\[Furey\]](#Furey){reference-type="ref" reference="Furey"}, with $\alpha_i$ replaced by $A_i$: $$\begin{aligned}
 \notag
     \Lambda_1 &= -A_2^\dagger A_1 - A_1^\dagger A_2 \notag \hspace{2em}
     \Lambda_2 = iA_2^\dagger A_1 -iA_1^\dagger A_2 \notag \hspace{2em}
     \Lambda_3 = A_2^\dagger A_2 - A_1^\dagger A \notag\\ 
     \Lambda_4 &= -A_1^\dagger A_3 - A_3^\dagger A_1 \notag \hspace{2em}
     \Lambda_5 = -iA_1^\dagger A_3 + iA_3^\dagger A_1 \notag \hspace{2em}
     \Lambda_6 = -A_3^\dagger A_2 - A_2^\dagger A_3 \notag\\
     \Lambda_7 &= iA_3^\dagger A_2 - iA_2^\dagger A_3 \notag \hspace{1em}
     \Lambda_8 = -\frac{1}{\sqrt{3}}(A_1^\dagger A_1 + A_2^\dagger A_2 - 2A_3^\dagger A_3), \notag
 
\end{aligned}$$ Furthermore, the number generator can again be used to define a $U(1)$ generator that assigns the correct electric charges to all the states: $$\begin{aligned}
\label{chargeQ}
    Q=\frac{N}{3}=\frac{1}{3}(A_1^{\dagger}A_1+A_2^{\dagger}A_2+A_3^{\dagger}A_3).
\end{aligned}$$
