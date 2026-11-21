---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-018-34-the-route-to-spin10-via-patisalam
section_title: "The Route to Spin(10) via Pati–Salam"
section_number: 3.4
pages: 55-62
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.997
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:route label="sec:route"}

In the last section, we showed how the Pati--Salam model answers two questions about the Standard Model:

> Why are quarks and leptons so similar? Why are left and right so different?

We were able to describe leptons as a fourth color of quark, 'white', and treat right-handed and left-handed particles on a more equal footing. Neither of these ideas worked on its own, but together, they made a full-fledged extension of the Standard Model, much like ${\rm SU}(5)$ and ${\rm Spin}(10)$, but based on seemingly different principles.

Yet thinking of leptons as 'white' should be strangely familiar, not just from the Pati--Salam perspective, but from the binary code that underlies both the ${\rm SU}(5)$ and the ${\rm Spin}(10)$ theories. There, leptons were indeed white: they all have color $r \wedge g \wedge b \in \Lambda{\mathbb C}^5$.

Alas, while ${\rm SU}(5)$ hints that leptons might be a fourth color, it does not deliver on this. The quark colors $$r, g, b \in \Lambda^1 {\mathbb C}^5$$ lie in a different irrep of ${\rm SU}(5)$ than does $r \wedge g \wedge b \in \Lambda^3
{\mathbb C}^5$. So, leptons in the ${\rm SU}(5)$ theory are white, but unlike the Pati--Salam model, this theory does not unify leptons with quarks.

Yet ${\rm SU}(5)$ theory is not the only game in town when it comes to the binary code. We also have ${\rm Spin}(10)$, which acts on the same vector space as ${\rm SU}(5)$. As a representation of ${\rm Spin}(10)$, $\Lambda{\mathbb C}^5$ breaks up into just two irreps: the even grades, $\Lambda^{\rm ev}{\mathbb C}^5$, which contain the left-handed particles and antiparticles: $$\Lambda^{\rm ev}{\mathbb C}^5 \cong\langle \overline{\nu}_L \rangle \oplus \langle e^+_L \rangle \oplus \left\langle \! \begin{array}{c} u_L \\ d_L \end{array} \! \right\rangle\oplus \langle \overline{u}_L \rangle \oplus \left\langle \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right\rangle\oplus \langle \overline{d}_L \rangle$$ and the odd grades $\Lambda^{\rm odd}{\mathbb C}^5$, which contain the right-handed particles and antiparticles: $$\Lambda^{\rm odd}{\mathbb C}^5 \cong\langle \nu_R \rangle \oplus \langle e^-_R \rangle \oplus \left\langle \! \begin{array}{c} \overline{d}_R \\ \overline{u}_R \end{array} \! \right\rangle\oplus \langle u_R \rangle \oplus \left\langle \! \begin{array}{c} e^+_R \\ \overline{\nu}_R \end{array} \! \right\rangle\oplus \langle d_R \rangle.$$ Unlike ${\rm SU}(5)$, the ${\rm Spin}(10)$ GUT really does unify $r \wedge g \wedge b$ with the colors $r$, $g$ and $b$, because they both live in the irrep $\Lambda^{\rm odd}{\mathbb C}^5$.

In short, it seems that the ${\rm Spin}(10)$ GUT, which we built as an extension of the ${\rm SU}(5)$ GUT, somehow managed to pick up this feature of the Pati--Salam model. How does ${\rm Spin}(10)$ relate to Pati--Salam's gauge group ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$, exactly? In general, we only know there is a map ${\rm SU}(n) \to {\rm Spin}(2n)$, but in low dimensions, there is much more, because some groups coincide: $$\begin{aligned}
    {\rm Spin}(3) & \cong& {\rm SU}(2) \\
    {\rm Spin}(4) & \cong& {\rm SU}(2) \times {\rm SU}(2) \\
    {\rm Spin}(5) & \cong& \rm{Sp}(2) \\
    {\rm Spin}(6) & \cong& {\rm SU}(4) 
\end{aligned}$$ What really stands out is this: $${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \cong{\rm Spin}(4) \times {\rm Spin}(6) .$$

This brings out an obvious relationship between the Pati--Salam model and the ${\rm Spin}(10)$ theory, because the inclusion ${\rm SO}(4) \times {\rm SO}(6) \hookrightarrow
{\rm SO}(10)$ lifts to the universal covers, so we get a homomorphism $$\eta \colon{\rm Spin}(4) \times {\rm Spin}(6) \to {\rm Spin}(10).$$ A word of caution is needed here. While $\eta$ is the lift of an inclusion, it is not an inclusion itself: it is two-to-one. This is because the universal cover ${\rm Spin}(4) \times {\rm Spin}(6)$ of ${\rm SO}(4) \times {\rm SO}(6)$ is a four-fold cover, being a double cover on each factor.

So we can try to extend the symmetries ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$ to ${\rm Spin}(10)$, though this can only work if the kernel of $\eta$ acts trivially on the Pati--Salam representation. What is this representation like? There is an obvious representation of ${\rm Spin}(4) \times {\rm Spin}(6)$ that extends to a ${\rm Spin}(10)$ rep. Both ${\rm Spin}(4)$ and ${\rm Spin}(6)$ have Dirac spinor representations, so their product ${\rm Spin}(4) \times {\rm Spin}(6)$ has a representation on $\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3$. And in fact, the obvious map $$g \colon\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3 \to \Lambda{\mathbb C}^5$$ given by $$v \otimes w \mapsto v \wedge w$$ is an isomorphism compatible with the actions of ${\rm Spin}(4) \times {\rm Spin}(6)$ on these two spaces. More concisely, this square: $$\xymatrix{
{\rm Spin}(4) \times {\rm Spin}(6) \ar[r]^-\eta \ar[d] & {\rm Spin}(10) \ar[d] \\
{\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\rm U}(g)} & {\rm U}(\Lambda{\mathbb C}^5) \\
}$$ commutes.

We will prove this in a moment. First though, we must check that this representation of ${\rm Spin}(4) \times {\rm Spin}(6)$ is secretly just another name for the Pati--Salam representation of ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$ on the space we discussed in Section [\[sec:g(2,2,4)\]](#sec:g(2,2,4)){reference-type="ref" reference="sec:g(2,2,4)"}: $$\big(({\mathbb C}^2 \otimes {\mathbb C}) \; \oplus \; ({\mathbb C}\otimes {\mathbb C}^2)\big)
\; \otimes \; \big({\mathbb C}^4 \; \oplus \; {\mathbb C}^{4*}\big).$$ Checking this involves choosing an isomorphism between ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$ and ${\rm Spin}(4) \times {\rm Spin}(6)$. Luckily, we can choose one that works:

::: thm
[]{#thm:Pati--Salam2 label="thm:Pati--Salam2"} There exists an isomorphism of Lie groups $$\alpha \colon{\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \to 
{\rm Spin}(4) \times {\rm Spin}(6)$$ and a unitary operator $$k \colon\big(({\mathbb C}^2 \otimes {\mathbb C}) \oplus ({\mathbb C}\otimes {\mathbb C}^2)\big) 
\otimes  \big({\mathbb C}^4 \oplus {\mathbb C}^{4*}\big)
\;\;  \to \;\; \Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3$$ that make this square commute: $$\xymatrix{
{\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \ar[r]^-{\alpha} \ar[d] 
& {\rm Spin}(4) \times {\rm Spin}(6) \ar[d] \\
{\rm U}\left(\left(({\mathbb C}^2 \otimes {\mathbb C}) \oplus ({\mathbb C}\otimes {\mathbb C}^2)\right) 
\otimes \left({\mathbb C}^4  \oplus  {\mathbb C}^{4*}\right)\right) 
\ar[r]^-{{\rm U}(k)} & {\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \\
}$$ where the left vertical arrow is the Pati--Salam representation and the right one is a tensor product of Dirac spinor representations.
:::

*Proof.* We can prove this in pieces, by separately finding a unitary operator $$({\mathbb C}^2 \otimes {\mathbb C}) \oplus ({\mathbb C}\otimes {\mathbb C}^2) \cong\Lambda{\mathbb C}^2$$ that makes this square commute: $$\xymatrix{
{\rm SU}(2) \times {\rm SU}(2) \ar[r]^-\sim \ar[d] & {\rm Spin}(4) \ar[d] \\
{\rm U}({\mathbb C}^2 \otimes {\mathbb C}\oplus {\mathbb C}\otimes {\mathbb C}^2) \ar[r]^-\sim & {\rm U}(\Lambda{\mathbb C}^2) \\
}$$ and a unitary operator $${\mathbb C}^4 \oplus {\mathbb C}^{4*} \cong\Lambda{\mathbb C}^3$$ that make this square: $$\xymatrix{
{\rm SU}(4) \ar[r]^\sim \ar[d] & {\rm Spin}(6) \ar[d] \\
{\rm U}({\mathbb C}^4 \oplus {\mathbb C}^{4*}) \ar[r]^-\sim & {\rm U}(\Lambda{\mathbb C}^3) \\
}$$ commute.

First, the ${\rm Spin}(6)$ piece. It suffices to show that the Dirac spinor rep of ${\rm Spin}(6) \cong{\rm SU}(4)$ on $\Lambda{\mathbb C}^3$ is isomorphic to ${\mathbb C}^4 \oplus {\mathbb C}^{4*}$ as a rep of ${\rm SU}(4)$. We start with the action of ${\rm Spin}(6)$ on $\Lambda{\mathbb C}^3$. This breaks up into irreps: $$\Lambda{\mathbb C}^3 \cong\Lambda^{\rm ev}{\mathbb C}^3 \oplus \Lambda^{\rm odd}{\mathbb C}^3$$ called the **left-handed** and **right-handed Weyl spinors**, and these are dual to each other because 6 = 2 mod 4, by a theorem that can be found in Adams' lectures [@adams:lelg]. Call these representations $$\rho_{\rm{ev}}\colon{\rm Spin}(6) \to {\rm U}( \Lambda^{\rm ev}{\mathbb C}^3 ), \qquad 
   \rho_{\rm{odd}}\colon{\rm Spin}(6) \to {\rm U}( \Lambda^{\rm odd}{\mathbb C}^3 ).$$ Since these reps are dual, it suffices just to consider one of them, say $\rho_{\rm{odd}}$.

Passing to Lie algebras, we have a homomorphism $$d\rho_{\rm{odd}}\colon{\mathfrak{so}}(6) \to {\mathfrak{u}}(\Lambda^{\rm odd}{\mathbb C}^3) \cong{\mathfrak{u}}(4)
\cong{\mathfrak{u}}(1) \oplus {\mathfrak{su}}(4).$$ Homomorphic images of semisimple Lie algebras are semisimple, so the image of ${\mathfrak{so}}(6)$ must lie entirely in ${\mathfrak{su}}(4)$. In fact ${\mathfrak{so}}(6)$ is simple, so this nontrivial map must be an injection $$d\rho_{\rm{odd}}\colon{\mathfrak{so}}(6) \to {\mathfrak{su}}(4),$$ and because the dimension is 15 on both sides, this map is also onto. Thus $d\rho_{\rm{odd}}$ is an isomorphism of Lie algebras, so $\rho_{\rm{odd}}$ is an isomorphism of the simply connected Lie groups ${\rm Spin}(6)$ and ${\rm SU}(4)$: $$\rho_{\rm{odd}}\colon{\rm Spin}(6) \to {\rm SU}(\Lambda^{\rm odd}{\mathbb C}^3) \cong{\rm SU}(4).$$ Furthermore, under this isomorphism $$\Lambda^{\rm odd}{\mathbb C}^3 \cong{\mathbb C}^4$$ as a representation of ${\rm SU}(\Lambda^{\rm odd}{\mathbb C}^3) \cong{\rm SU}(4)$. Taking duals, we obtain an isomorphism $$\Lambda^{\rm ev}{\mathbb C}^3 \cong{\mathbb C}^{4*}$$ Putting these together, we get an isomorphism ${\mathbb C}^{4} \oplus {\mathbb C}^{4*} \cong
\Lambda{\mathbb C}^3$ that makes this square commute: $$\xymatrix{
{\rm Spin}(6) \ar[d] \ar[r]^\rho_{\rm{odd}}& {\rm SU}(4) \ar[d] \\
{\rm U}(\Lambda{\mathbb C}^3) \ar[r] & {\rm U}({\mathbb C}^4 \oplus {\mathbb C}^{4*})
}$$ which completes the proof for ${\rm Spin}(6)$.

Next, the ${\rm Spin}(4)$ piece. It suffices to show that the spinor rep $\Lambda{\mathbb C}^2$ of ${\rm Spin}(4) \cong{\rm SU}(2) \times {\rm SU}(2)$ is isomorphic to ${\mathbb C}^2 \otimes {\mathbb C}\; \oplus \; {\mathbb C}\otimes {\mathbb C}^2$ as a rep of ${\rm SU}(2)
\times {\rm SU}(2)$. We start with the action of ${\rm Spin}(4)$ on $\Lambda{\mathbb C}^2$. This again breaks up into irreps: $$\Lambda{\mathbb C}^2 \cong\Lambda^{\rm odd}{\mathbb C}^2 \oplus \Lambda^{\rm ev}{\mathbb C}^2.$$ Again we call these representations $$\rho_{\rm{ev}}\colon{\rm Spin}(4) \to {\rm U}( \Lambda^{\rm ev}{\mathbb C}^2 ) , \qquad
 \rho_{\rm{odd}}\colon{\rm Spin}(4) \to {\rm U}( \Lambda^{\rm odd}{\mathbb C}^2 ) .$$

First consider $\rho_{\rm{ev}}$. Passing to Lie algebras, this gives a homomorphism $$d\rho_{\rm{ev}}\colon{\mathfrak{so}}(4) \to {\mathfrak{u}}(\Lambda^{\rm ev}{\mathbb C}^2) \cong{\mathfrak{u}}(2) \cong{\mathfrak{u}}(1) \oplus {\mathfrak{su}}(2)$$ Homomorphic images of semisimple Lie algebras are semisimple, so the image of ${\mathfrak{so}}(4)$ must lie entirely in ${\mathfrak{su}}(2)$. Similarly, $d\rho_{\rm{odd}}$ also takes ${\mathfrak{so}}(4)$ to ${\mathfrak{su}}(2)$: $$d\rho_{\rm{odd}}\colon{\mathfrak{so}}(4) \to {\mathfrak{su}}(2)$$ and we can combine these maps to get $$d\rho_{\rm{odd}}\oplus d\rho_{\rm{ev}}\colon{\mathfrak{so}}(4) \to {\mathfrak{su}}(2) \oplus {\mathfrak{su}}(2),$$ which is just the derivative of ${\rm Spin}(4)$'s representation on $\Lambda{\mathbb C}^2$. Since this representation is faithful, the map $d\rho_{\rm{odd}}\oplus d\rho_{\rm{ev}}$ of Lie algebras is injective. But the dimensions of ${\mathfrak{so}}(4)$ and ${\mathfrak{su}}(2) \oplus
{\mathfrak{su}}(2)$ agree, so $d\rho_{\rm{odd}}\oplus d\rho_{\rm{ev}}$ is also onto. Thus it is an isomorphism of Lie algebras. This implies that $\rho_{\rm{odd}}\oplus \rho_{\rm{ev}}$ is an isomorphism of the simply connected Lie groups ${\rm Spin}(4)$ and ${\rm SU}(2) \times {\rm SU}(2)$ $$\rho_{\rm{odd}}\oplus \rho_{\rm{ev}}\colon{\rm Spin}(4) \to {\rm SU}(\Lambda^{\rm odd}{\mathbb C}^2) \times {\rm SU}(\Lambda^{\rm ev}{\mathbb C}^2) \cong{\rm SU}(2) \times {\rm SU}(2)$$ under which ${\rm SU}(2) \times {\rm SU}(2)$ acts on $\Lambda^{\rm odd}{\mathbb C}^2 \oplus \Lambda^{\rm ev}{\mathbb C}^2$. The left factor of ${\rm SU}(2)$ acts irreducibly on $\Lambda^{\rm odd}{\mathbb C}^2$, which the second factor is trivial on. Thus $\Lambda^{\rm odd}{\mathbb C}^2 \cong
{\mathbb C}^2 \otimes {\mathbb C}$ as a rep of ${\rm SU}(2) \times {\rm SU}(2)$. Similarly, $\Lambda^{\rm ev}{\mathbb C}^2
\cong{\mathbb C}\otimes {\mathbb C}^2$ as a rep of this group. Putting these together, we get an isomorphism ${\mathbb C}^2 \otimes {\mathbb C}\oplus {\mathbb C}\otimes {\mathbb C}^2 \cong
\Lambda{\mathbb C}^2$ that makes this square commute: $$\xymatrix{
{\rm Spin}(4) \ar[d] \ar[r]^-{\rho_{\rm{ev}}\oplus \rho_{\rm{odd}}} & {\rm SU}(2) \times {\rm SU}(2) \ar[d] \\
{\rm U}(\Lambda{\mathbb C}^2) \ar[r] & {\rm U}({\mathbb C}^2 \otimes {\mathbb C}\oplus {\mathbb C}\otimes {\mathbb C}^2)
}$$ which completes the proof for ${\rm Spin}(4)$. 3em $\sqcap$ -1em $\sqcup$ 2ex

In the proof of the preceding theorem, we merely showed that there *exists* an isomorphism $$k \colon\big(({\mathbb C}^2 \otimes {\mathbb C}) \oplus
({\mathbb C}\otimes {\mathbb C}^2)\big) \otimes \big({\mathbb C}^4 \oplus {\mathbb C}^{4*}\big) \to \Lambda{\mathbb C}^2
\otimes \Lambda{\mathbb C}^3$$ making the square commute. We did not say exactly what $k$ was. In the proof, we built it after quietly choosing three unitary operators, giving these isomorphisms: $${\mathbb C}^2 \otimes {\mathbb C}\cong\Lambda^{\rm odd}{\mathbb C}^2, \quad {\mathbb C}\otimes {\mathbb C}^2 \cong\Lambda^{\rm ev}{\mathbb C}^2, \quad {\mathbb C}^4 \cong\Lambda^{\rm odd}{\mathbb C}^3.$$ Since the remaining map $\Lambda^{\rm ev}{\mathbb C}^3 \cong{\mathbb C}^{4*}$ is determined by duality, these three operators determine $k$, and they also determine the Lie group isomorphism $\alpha$ via the construction in our proof.

There is, however, a specific choice for these unitary operators that we prefer, because this choice makes the particles in the Pati--Salam representation $\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3$ look almost exactly like those in the ${\rm SU}(5)$ representation $\Lambda{\mathbb C}^5$.

First, since ${\mathbb C}^2 = \Lambda^1 {\mathbb C}^2 = \Lambda^{\rm odd}{\mathbb C}^2$ is spanned by $u$ and $d$, the (left-handed) isospin states of the Standard Model, we really ought to identify the left-isospin states $u_L$ and $d_L$ of the Pati--Salam model with these. So, we should use this unitary operator: $$\begin{array}{ccl}
 {\mathbb C}^2 \otimes {\mathbb C}& \stackrel{\sim}{\longrightarrow} &  \Lambda^{\rm odd}{\mathbb C}^2  \\
             u_L & \mapsto & u   \\
             d_L & \mapsto & d .
\end{array}$$

Next, we should use this unitary operator for right-isospin states: $$\begin{array}{ccl}
 {\mathbb C}\otimes {\mathbb C}^2 & \stackrel{\sim}{\longrightarrow} &  \Lambda^{\rm ev}{\mathbb C}^2  \\
             u_R & \mapsto & u \wedge d   \\
             d_R & \mapsto & 1 .
\end{array}$$ Why? Because the right-isospin up particle is the right-handed neutrino $\nu_R$, which corresponds to $u \wedge d \wedge r \wedge g \wedge b$ in the ${\rm SU}(5)$ theory, but $u_R \otimes w$ in the Pati--Salam model. This suggests that $u \wedge d$ and $u_R$ should be identified.

Finally, because ${\mathbb C}^3$ is spanned by the colors $r$, $g$ and $b$, while ${\mathbb C}^4$ is spanned by the colors $r$, $g$, $b$ and $w$, we really ought to use this unitary operator: $$\begin{array}{ccl}
 {\mathbb C}^4 & \stackrel{\sim}{\longrightarrow} &  \Lambda^{\rm odd}{\mathbb C}^3  \\
    r & \mapsto & r \\ 
    g & \mapsto & g \\ 
    b & \mapsto & b \\ 
    w & \mapsto & r \wedge g \wedge b 
\end{array}$$ Dualizing this, we get the unitary operator $$\begin{array}{ccl}
 {\mathbb C}^{4*} & \stackrel{\sim}{\longrightarrow} &  \Lambda^{\rm ev}{\mathbb C}^3  \\
    \overline{r} & \mapsto & g \wedge b \\ 
    \overline{g} & \mapsto & b \wedge r \\ 
    \overline{b} & \mapsto & r \wedge g \\ 
    \overline{w} & \mapsto & 1
\end{array}$$

These choices determine the unitary operator $$k \colon\big(({\mathbb C}^2 \otimes {\mathbb C})
\oplus ({\mathbb C}\otimes {\mathbb C}^2)\big) \otimes \big({\mathbb C}^4 \oplus {\mathbb C}^{4*}\big)
\to \Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3  .$$ With this specific choice of $k$, we can combine the commutative squares built in Theorems [\[thm:Pati\--Salam\]](#thm:Pati--Salam){reference-type="ref" reference="thm:Pati--Salam"} and [\[thm:Pati\--Salam2\]](#thm:Pati--Salam2){reference-type="ref" reference="thm:Pati--Salam2"}: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^-{\beta} \ar[d] 
& {\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \ar[r]^-{\alpha} \ar[d] 
& {\rm Spin}(4) \times {\rm Spin}(6) \ar[d]
\\
{\rm U}( F \oplus F^* ) \ar[r]^-{U(\ell)} 
& {\rm U}\left(\big(({\mathbb C}^2 \otimes {\mathbb C}) \oplus ({\mathbb C}\otimes {\mathbb C}^2)\big)
\otimes \big({\mathbb C}^4 \oplus {\mathbb C}^{4*}\big)\right) \ar[r]^-{{\rm U}(k)} 
& {\rm U}(\Lambda {\mathbb C}^5) 
}$$ to obtain the following result:

::: thm
[]{#thm:Pati--Salam3 label="thm:Pati--Salam3"} Taking $\theta = \alpha \beta$ and $h = k \ell$, the following square commutes: $$\xymatrix{
        {G_{\mbox{\rm SM}}}\ar[r]^-\theta \ar[d]       & {\rm Spin}(4) \times {\rm Spin}(6) \ar[d] \\
        {\rm U}(F \oplus F^*) \ar[r]^-{{\rm U}(h)} & {\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \\
        }$$ where the left vertical arrow is the Standard Model representation and the right one is a tensor product of Dirac spinor representations.
:::

The map $h$, which tells us how to identify $F \oplus F^*$ and $\Lambda{\mathbb C}^2
\otimes \Lambda{\mathbb C}^3$, is given by applying $k$ to the 'Pati--Salam code' in Table [\[tab:pscode1\]](#tab:pscode1){reference-type="ref" reference="tab:pscode1"}. This gives a binary code for the Pati--Salam model: 1em

::: center
::: {#tab:pscode2}
                     **The Binary Code for Pati--Salam**                                                                                                                                                                      
  ------------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------------------------------------------------------ -----------------------------------------------------------------------
   $\Lambda^{\rm odd}{\mathbb C}^2 \otimes \Lambda^{\rm odd}{\mathbb C}^3$   $\Lambda^{\rm ev}{\mathbb C}^2 \otimes \Lambda^{\rm odd}{\mathbb C}^3$   $\Lambda^{\rm odd}{\mathbb C}^2 \otimes \Lambda^{\rm ev}{\mathbb C}^3$   $\Lambda^{\rm ev}{\mathbb C}^2 \otimes \Lambda^{\rm ev}{\mathbb C}^3$
                           $\nu_L = u \otimes rgb$                                                  $\nu_R = ud \otimes rgb$                                              $e^+_R         = u \otimes 1$                                           $e^+_L         = ud \otimes 1$
                           $e^-_L = d \otimes rgb$                                                  $e^-_R = 1 \otimes rgb$                                           $\overline{\nu}_R      = d \otimes 1$                                    $\overline{\nu}_L      = 1 \otimes 1$
                            $u^c_L = u \otimes c$                                                    $u^c_R = ud \otimes c$                                 $\overline{d}^{\overline{c}}_R = u \otimes {\overline{c}}$              $\overline{d}^{\overline{c}}_L = ud \otimes {\overline{c}}$
                            $d^c_L = d \otimes c$                                                    $d^c_R = 1 \otimes c$                                  $\overline{u}^{\overline{c}}_R = d \otimes {\overline{c}}$              $\overline{u}^{\overline{c}}_L = 1 \otimes {\overline{c}}$

  : Pati--Salam binary code for first-generation fermions, where $c = r, g, b$ and ${\overline{c}}= gb, br, rg$.
:::
:::

-1em We have omitted wedge product symbols to save space. Note that if we apply the obvious isomorphism $$g \colon\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3 \to \Lambda{\mathbb C}^5$$ given by $$v \otimes w \mapsto v \wedge w$$ then the above table does more than merely resemble Table [\[tab:su5code\]](#tab:su5code){reference-type="ref" reference="tab:su5code"}, which gives the binary code for the ${\rm SU}(5)$ theory. The two tables become *identical!*

This fact is quite intriguing. We will explore its meaning in the next section. But first, let us start by relating the Pati--Salam model to the ${\rm Spin}(10)$ theory:

::: thm
[]{#thm:Spin(10) label="thm:Spin(10)"} The following square commutes: $$\xymatrix{
{\rm Spin}(4) \times {\rm Spin}(6) \ar[r]^-\eta \ar[d] & {\rm Spin}(10) \ar[d] \\
{\rm U}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\rm U}(g)} & {\rm U}(\Lambda{\mathbb C}^5)
}$$ where the right vertical arrow is the Dirac spinor representation, the left one is the tensor product of Dirac spinor representations, and $$\eta \colon{\rm Spin}(4) \times {\rm Spin}(6) \to {\rm Spin}(10)$$ is the homomorphism lifting the inclusion of ${\rm SO}(4) \times {\rm SO}(6)$ in ${\rm SO}(10)$.
:::

*Proof*. At the Lie algebra level, we have the inclusion $${\mathfrak{so}}(4) \oplus {\mathfrak{so}}(6) \hookrightarrow{\mathfrak{so}}(10)$$ by block diagonals, which is also just the differential of the inclusion ${\rm SO}(4) \times {\rm SO}(6) \hookrightarrow{\rm SO}(10)$ at the Lie group level. Given how the spinor reps are defined in terms of creation and annihilation operators, it is easy to see that $$\xymatrix{
{\mathfrak{so}}(4) \oplus {\mathfrak{so}}(6) \ar@{^{(}->}[r] \ar[d] & {\mathfrak{so}}(10) \ar[d] \\
{\mathfrak{gl}}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\mathfrak{gl}}(g)}  & {\mathfrak{gl}}(\Lambda{\mathbb C}^5) \\
}$$ commutes, because $g$ is an intertwining operator between representations of ${\mathfrak{so}}(4) \oplus {\mathfrak{so}}(6)$. That is because the ${\mathfrak{so}}(4)$ part only acts on $\Lambda{\mathbb C}^2$, while the ${\mathfrak{so}}(6)$ part only acts on $\Lambda{\mathbb C}^3$.

But these Lie algebras act by skew-adjoint operators, so really $$\xymatrix{
{\mathfrak{so}}(4) \oplus {\mathfrak{so}}(6) \ar@{^{(}->}[r] \ar[d] & {\mathfrak{so}}(10) \ar[d] \\
{\mathfrak{u}}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\mathfrak{u}}(g)}  & {\mathfrak{u}}(\Lambda{\mathbb C}^5) \\
}$$ commutes. Since the ${\mathfrak{so}}(n)$'s and their direct sums are semisimple, so are their images. Therefore, their images live in the semisimple part of the unitary Lie algebras, which is just another way of saying the special unitary Lie algebras. We get that $$\xymatrix{
{\mathfrak{so}}(4) \oplus {\mathfrak{so}}(6) \ar@{^{(}->}[r] \ar[d] & {\mathfrak{so}}(10) \ar[d] \\
{\mathfrak{su}}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\mathfrak{su}}(g)}  & {\mathfrak{su}}(\Lambda{\mathbb C}^5) \\
}$$ commutes, and this gives a commutative square in the world of simply connected Lie groups: $$\xymatrix{
{\rm Spin}(4) \times {\rm Spin}(6) \ar[r]^-\eta \ar[d] & {\rm Spin}(10) \ar[d] \\
{\rm SU}(\Lambda{\mathbb C}^2 \otimes \Lambda{\mathbb C}^3) \ar[r]^-{{\rm SU}(g)} & {\rm SU}(\Lambda{\mathbb C}^5)
}$$ This completes the proof. 3em $\sqcap$ -1em $\sqcup$ 2ex

This result shows us how to reach the ${\rm Spin}(10)$ theory, not through the ${\rm SU}(5)$ theory, but through the Pati--Salam model. For physics texts that treat this issue, see for example Zee [@zee:nutshell] and Ross [@ross:gut].
