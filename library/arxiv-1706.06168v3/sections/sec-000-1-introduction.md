---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.991
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
In 1914, Pólya and Schur [@polya1914zwei] characterized the set of diagonal linear operators on polynomials which preserve real-rootedness. Since this seminal paper, much work has been done in extending this characterization to other classes of linear operators. This program in essence came to a close in 2009 with a paper of Borcea and Brändén [@bb1], which gave a complete characterization of linear operators on polynomials which preserve real-rootedness.

Their real-rootedness preservation characterization is derived from a more general result pertaining to stable polynomials. Given $\Omega \subset \mathbb{C}^m$, we say that a polynomial $f \in \mathbb{C}[x_1,\ldots,x_m]$ is *$\Omega$-stable* if $f$ does not vanish in $\Omega$. Further, $f$ is *real stable* if it has real coefficients and is $\mathcal{H}_+^m$-stable, where $\mathcal{H}_+\subset \mathbb{C}$ is the open upper half-plane. (We also denote the open lower half-plane by $\mathcal{H}_-\subset \mathbb{C}$.) We additionally use the terms *weakly* $\Omega$-stable and *weakly* real stable if we allow $f \equiv 0$. Finally, we write $f \in \mathbb{C}^\lambda[x_1,\ldots,x_m]$ for $\lambda \equiv (\lambda_1,\ldots,\lambda_m)$ if $f$ is of degree at most $\lambda_k$ in $x_k$. We are then led to the following problems for $\mathbb{K}\in \{\mathbb{C},\mathbb{R}\}$, generalized from the Pólya-Schur characterization:

::: problem
Characterize linear operators $T: \mathbb{K}^\lambda[x_1,\ldots,x_m] \to \mathbb{K}[x_1,\ldots,x_m]$ preserving weak $\Omega$-stability.
:::

::: problem
Characterize linear operators $T: \mathbb{K}[x_1,\ldots,x_m] \to \mathbb{K}[x_1,\ldots,x_m]$ preserving weak $\Omega$-stability.
:::

In [@bb1], Borcea and Brändén were able to solve these problems in many cases. In particular, they solved both problems for $\mathbb{K}= \mathbb{R}$ and $\Omega = \mathcal{H}_+^m$, where $m=1$ corresponds to the case of preservation of real-rooted polynomials. For $\mathbb{K}= \mathbb{C}$, they were able to solve Problem 1 for $\Omega$ that is *any* product of open circular regions in $\mathbb{C}$.

In this paper we will only be concerned with Problem 1, for which we now state the solution from [@bb1]. Given a linear operator $T: \mathbb{K}^\lambda[x_1,\ldots,x_m] \to \mathbb{K}[x_1,\ldots,x_m]$, a polynomial $\mathop{\mathrm{Symb}}_{BB}(T)$ called the *(Borcea-Brändén) symbol* is associated to $T$. Specifically, the symbol is a polynomial in $\mathbb{K}^{\lambda \sqcup \lambda}[x_1,\ldots,x_m, z_1,\ldots,z_m]$ (i.e., of $2m$ variables), where $\lambda \sqcup \lambda := (\lambda_1,\ldots,\lambda_m,\lambda_1,\ldots,\lambda_m)$. The crucial feature of the symbol is that it shares certain stability properties with its associated linear operator, which yields the characterizations stated in the following results. (We will express these results in more detail in §[\[Cops_sect\]](#Cops_sect){reference-type="ref" reference="Cops_sect"} and §[\[Rops_sect\]](#Rops_sect){reference-type="ref" reference="Rops_sect"}.)

::: theorem
[]{#BB_Cops_thm label="BB_Cops_thm"} Fix a linear operator $T: \mathbb{C}^\lambda[x_1,\ldots,x_m] \to \mathbb{C}[x_1,\ldots,x_m]$ which has image of dimension greater than one. Then, $T$ maps $\mathcal{H}_+^m$-stable polynomials to weakly $\mathcal{H}_+^m$-stable polynomials if and only if $\mathop{\mathrm{Symb}}_{BB}(T)$ is $\mathcal{H}_+^{2m}$-stable.
:::

::: theorem
[]{#BB_Rops_thm label="BB_Rops_thm"} Fix a linear operator $T: \mathbb{R}^\lambda[x_1,\ldots,x_m] \to \mathbb{R}[x_1,\ldots,x_m]$ which has image of dimension greater than two. Then, $T$ maps real stable polynomials to weakly real stable polynomials if and only if either $\mathop{\mathrm{Symb}}_{BB}(T)$ or $\mathop{\mathrm{Symb}}_{BB}(T^-)$ is real stable, where $T^-(p) := T(p(-x_1,\ldots,-x_m))$.
:::

To deal with other products of circular regions, one then conjugates $T$ by certain Möbius transformations and applies Theorem [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} to the conjugated operator. Unfortunately though, this is a tedious process which has to be done each time a new stability region is to be considered. Additionally, the image dimension restrictions give rise to degeneracy cases which have to be dealt with separately. Both of these issues obscure the connection between an operator and its symbol.

In this paper, we present a new conceptual approach to the Borcea-Brändén characterization via the representation theory of $\mathop{\mathrm{SL}}_2(\mathbb{C})$. In particular, we derive a new symbol (denoted $\mathop{\mathrm{Symb}}$) in a natural way, and our definition eliminates the issues discussed above. This is seen in the following results, which are our simplified and generalized versions of the Borcea-Brändén characterizations. Note that for the sake of simplicity, we have omitted a few details here regarding non-convex circular regions. Specifically, circular regions of $\mathbb{C}$ should be thought of as lying in the Riemann sphere, so that complements of discs contain the point at $\infty$.

::: Cops_graces
**Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"} 1**. *Fix a linear operator $T: \mathbb{C}^\lambda[x_1,\ldots,x_m] \to \mathbb{C}^\alpha[x_1,\ldots,x_l]$, a product of all open or all closed circular regions $\Omega_0 = C_1 \times \cdots \times C_m$, and a product of sets $\Omega_1 := S_1 \times \cdots \times S_m$. Further, denote $\widetilde{\Omega}_0 := (\mathbb{C}\setminus C_1) \times \cdots \times (\mathbb{C}\setminus C_m)$. Up to certain degree and convexity (of $C_k$) restrictions, we have that $T$ maps $\Omega_0$-stable polynomials to nonzero $\Omega_1$-stable polynomials if and only if $\mathop{\mathrm{Symb}}(T)$ is $(\widetilde{\Omega}_0 \times \Omega_1)$-stable.*
:::

::: Rops_graces
**Theorem [\[Rops_graces\]](#Rops_graces){reference-type="ref" reference="Rops_graces"} 1**. *Fix a linear operator $T: \mathbb{R}^\lambda[x_1,\ldots,x_m] \to \mathbb{R}^\alpha[x_1,\ldots,x_l]$. Up to certain degree restrictions, $T$ maps real stable polynomials to nonzero real stable polynomials if and only if $\mathop{\mathrm{Symb}}(T)$ is either $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_+^l)$-stable or $(\overline{\mathcal{H}_-}^m \times \mathcal{H}_-^l)$-stable.*
:::

We summarize the specific improvements that this and our other related results give over the Borcea-Brändén characterization as follows.

1.  *Different stability regions can be considered using the same symbol.* The symbol we define in this paper is universal: for example, it gives stability-preservation information for *any* product of open circular regions. The Borcea-Brändén symbol, on the other hand, required the application of Möbius transformations. In addition, our symbol also allows for the output stability region to be chosen independently of the input stability region. While this does not literally improve the result, it does allow for quicker computations. In particular, see Examples [\[add_conv_ex1\]](#add_conv_ex1){reference-type="ref" reference="add_conv_ex1"} and [\[mult_conv_ex1\]](#mult_conv_ex1){reference-type="ref" reference="mult_conv_ex1"} where classical polynomial convolution results are easily derived from our framework.

2.  *Our characterization does not require any degeneracy condition.* Our results characterize operators which preserve (strong) stability rather than weak stability. As seen above, this slightly stronger notion of stability enables us to eliminate any image dimension degeneracy condition, as required in the Borcea-Brändén characterizations (Theorems [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} and [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"}). This demonstrates a cleaner link between an operator and its symbol.

3.  *Closed circular regions and projectively convex regions can be considered.* The symbol we define in this paper handles products of open circular regions, as well as products of closed circular regions. (In [@melamud2015ops], Melamud proves a result similar to the Borcea-Brändén characterization for closed circular regions.) Further, we are also able to consider more general *projectively convex* regions (circular regions with portions of their boundary; also called *generalized circular regions*, see [@zervos1960aspects] and [@zaheer1976polar]) in Proposition [\[Cops_prop\]](#Cops_prop){reference-type="ref" reference="Cops_prop"}. This allows us to determine stability-preservation information about real intervals and half-lines. It also turns out, somewhat surprisingly, that our symbol can handle products of any *sets* as possible output space stability regions (as seen in Theorem [\[Cops_graces\]](#Cops_graces){reference-type="ref" reference="Cops_graces"} above).

In the process of generalizing the Borcea-Brändén characterization we develop a general algebraic framework which also encompasses many of the classical polynomial tools. This framework aims to motivate classical results and provide intuition for the connection between a stability preserving operator and its symbol.

### The Main Idea

A major purpose of this paper is to explain a certain conceptual thread in the history of polynomial stability theory: that it is often possible to determine general stability information from restricted sets of polynomials. For example, the Pólya-Schur and Borcea-Brändén characterizations derive from a single polynomial (i.e., the symbol) stability properties of a whole collection of polynomials in the output of a given linear operator. Additionally, the Grace-Walsh-Szegő coincidence theorem says that stability information of any polynomial can be determined from its polarization, which is of degree at most one in each variable.

As it turns out, these sorts of phenomena can be explained using relatively basic algebraic and representation theoretic concepts. We view $\mathbb{C}^n[x]$ as a representation of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ via the standard action, given as follows. For $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ and $f \in \mathbb{C}^n[x]$, we define: $$(\phi \cdot f)(x) := f(\phi^{-1}x)$$ Here $\phi^{-1}$ acts on $x \in \mathbb{C}$ as a Möbius transformation, or equivalently $\phi$ acts on the roots of $f$. (Similarly, $\mathbb{C}^\lambda[x_1,\ldots,x_m]$ can be viewed as a representation of $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$ via this action in each variable.) Under this interpretation, important maps like polarization, projection, the apolarity form, and even the symbol turn out to be invariant under these $\mathop{\mathrm{SL}}_2(\mathbb{C})$ actions. This leads us to a conceptual thesis: *$\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant maps transfer stability information*.

The goal of this paper is then to explicate and answer the most important question related to this thesis: what does it mean for the symbol map to be $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant and how does it transfer stability information? To answer this, we consider the following standard ideas relating spaces of linear operators to tensor products.

Let $W_1,W_2$ be two finite dimensional representations of a group $G$, and let $\mathop{\mathrm{Hom}}(W_1,W_2)$ denote the space of linear maps from $W_1$ to $W_2$. Then, $\mathop{\mathrm{Hom}}(W_1,W_2) \cong W_1^* \boxtimes W_2$ (the outer tensor product) can viewed as a representation of $G \times G$. If we further have a $G$-invariant bilinear form on $W_1$, then we also have $W_1 \cong W_1^*$. This leads to the following identification: $$\mathop{\mathrm{Hom}}(W_1,W_2) \cong W_1^* \boxtimes W_2 \cong W_1 \boxtimes W_2$$ If $W_1$ and $W_2$ are spaces of polynomials, each in $m$ variables, then their tensor product $W_1 \boxtimes W_2$ is isomorphic to a larger space of polynomials in $2m$ variables. That is, a linear operator between polynomial spaces $W_1$ and $W_2$ can be associated to some polynomial in double the variables, via the above identification of representations. This is precisely the idea of the symbol of an operator.

Let's see how this works in the univariate case. Consider $\mathbb{C}^n[x]$ as a representation of the group $\mathop{\mathrm{SL}}_2(\mathbb{C})$, as described above. It is then a standard result that the classical bilinear *apolarity form* is invariant under the action of Möbius transformations. That is, the apolarity form is an $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant bilinear form on $\mathbb{C}^n[x]$. This form, applied to $f,g \in \mathbb{C}^n[x]$ with coefficients $f_k,g_k$, is defined as follows: $$\langle f,g \rangle^n := \sum_{k=0}^n \binom{n}{k}^{-1} (-1)^k f_k g_{n-k}$$ With this, we obtain the identification described above: $\mathop{\mathrm{Hom}}(\mathbb{C}^n[x],\mathbb{C}^m[x]) \cong \mathbb{C}^n[x] \boxtimes \mathbb{C}^m[x] \cong \mathbb{C}^{(n,m)}[x,z]$. The final piece of the puzzle is then to find a way to transfer stability information through this identification of representations. The key result to this end is the classical Grace's theorem:

::: ref_theorem
Let $f,g \in \mathbb{C}^n[x]$ be polynomials of degree exactly $n$. Further, let $C$ be some open or closed circular region such that $f$ is $C$-stable and $g$ is $(\mathbb{C}\setminus C)$-stable. Then, $\langle f,g \rangle^n \neq 0$.
:::

That is, the apolarity form not only provides the link between a linear operator and its symbol, but also captures stability information. So, whatever stability claims we can make about polynomials in $\mathbb{C}^{(n,m)}[x,z]$ can then be seamlessly transferred to corresponding linear operators in $\mathop{\mathrm{Hom}}(\mathbb{C}^n[x],\mathbb{C}^m[x])$. From this we are able to recover the Borcea-Brändén characterization. Additionally, all of the theory here relating stability and the representation theory of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ can be generalized to multivariate polynomials in a straightforward manner. The details will be discussed in §[\[reps_sect\]](#reps_sect){reference-type="ref" reference="reps_sect"}.

In a similar fashion, other important maps also have $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariance properties (e.g., polarization and projection, as used in the Grace-Walsh-Szegő coincidence theorem, explicitly give the isomorphisms of a classical representation theoretic result; see Appendix [\[gws_app\]](#gws_app){reference-type="ref" reference="gws_app"}). A main feature of our conceptual thesis is that it allows for a unification of many seemingly related results in polynomial stability theory. A crucial point to make then is that Grace's theorem is at the heart of this unification. That said, a significant portion of this paper is devoted to discussing it.

### A Generalized Grace's Theorem and Interval- and Ray-Rootedness

In [@bb2], Borcea and Brändén are able to prove a multivariate Grace's theorem using their operator characterization. In this paper we will prove the multivariate version from scratch, and then use it to derive a new characterization of stability-preserving linear operators. In addition, we generalize it to *projectively convex* regions, which consist of an open circular region with a portion of its boundary (see §[\[proj_conv_subsect\]](#proj_conv_subsect){reference-type="ref" reference="proj_conv_subsect"}). We state our new result as follows. Note that this result can be seen as an extension of the generalized Grace's theorem given in Corollary 4.4 of [@zaheer1976polar].

::: graces_thm
**Theorem [\[graces_thm\]](#graces_thm){reference-type="ref" reference="graces_thm"} 1**. *Fix $\lambda \in \mathbb{N}_0^m$ and $f,g \in \mathbb{C}^\lambda[x_1,\ldots,x_m]$ such that $f$ and $g$ both have a nonzero term of degree $\lambda$. Also, denote $C := \mathcal{H}_+\cup \overline{\mathbb{R}_+}$ and $\widetilde{C} := \mathcal{H}_-\cup \overline{\mathbb{R}_-}$. If $f$ is $C^m$-stable and $g$ is $\widetilde{C}^m$-stable, then $\langle f,g \rangle^\lambda \neq 0$.*
:::

This result can, for instance, give stability information about positive- and negative-rooted polynomials. Since the apolarity form is invariant under the action of Möbius transformations, we immediately obtain similar statements regarding the union of any open circular region and a portion of its boundary. Notice also that, unlike the classical Grace's theorem, the stability regions $C$ and $\widetilde{C}$ have non-empty intersection.

In the vein of this extension, we provide a new characterization of a certain class of linear operators which preserve ray- and interval-rootedness. The problem of classifying all such operators is still open in general (see e.g., the end of [@bba]). Here, we solve this problem for a restricted class of operators: namely, operators which both preserve weak real-rootedness and also preserve ray- or interval-rootedness. Our main result in this direction is stated as follows, where a polynomial is called $J$-rooted when all of its roots are in $J$:

::: Jops_graces
**Theorem [\[Jops_graces\]](#Jops_graces){reference-type="ref" reference="Jops_graces"} 1**. *Fix a linear operator $T: \mathbb{R}^n[x] \to \mathbb{R}^m[x]$ which has image of dimension greater than two. Further, let $I,J \subseteq \mathbb{R}$ be intervals or rays. Up to certain degree restrictions, $T$ preserves weak real-rootedness and maps $I$-rooted polynomials to nonzero $J$-rooted polynomials if and only if $\mathop{\mathrm{Symb}}(T)$ is either $(\mathcal{H}_-\cup I) \times (\overline{\mathcal{H}_+} \setminus J)$-stable or $(\mathcal{H}_-\cup I) \times (\overline{\mathcal{H}_-} \setminus J)$-stable.*
:::

In §[\[Jops_subsect\]](#Jops_subsect){reference-type="ref" reference="Jops_subsect"}, this result is stated in a more restricted manner as the degeneracy condition (image dimension) and degree restrictions end up being more tedious than in the other results. Corollary [\[Jops_graces_cor\]](#Jops_graces_cor){reference-type="ref" reference="Jops_graces_cor"} and further explication then give the result as stated here.

As a final note, all of the results given here in the introduction are stated slightly differently in §[\[graces_sect\]](#graces_sect){reference-type="ref" reference="graces_sect"}, §[\[Cops_sect\]](#Cops_sect){reference-type="ref" reference="Cops_sect"}, §[\[Rops_sect\]](#Rops_sect){reference-type="ref" reference="Rops_sect"}. In particular, the notation $V(\lambda)$ is used in place of $\mathbb{C}^\lambda[x_1,\ldots,x_m]$, and reference is made to $\mathbb{CP}^1$ (i.e., the Riemann sphere). This notation has to do with consideration of "roots at infinity", which allows us to remove degree restrictions and avoid reference to convex circular regions. We discuss this rigorously in §[\[homog_subsect\]](#homog_subsect){reference-type="ref" reference="homog_subsect"}.

### A Roadmap

We now describe the content of the remainder of this paper. In §[\[prelim_sect\]](#prelim_sect){reference-type="ref" reference="prelim_sect"}, we discuss the use of homogeneous polynomials via the notation $V(n)$ and $V(\lambda)$, and we describe the relation of these spaces to the notion of roots at infinity.

In §[\[reps_sect\]](#reps_sect){reference-type="ref" reference="reps_sect"}, we explicate some very basic representation theory of $\mathop{\mathrm{SL}}_2(\mathbb{C})$. We then demonstrate how the apolarity form and the symbol arise as natural constructs in this context. Results like the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}) and the $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariance of the apolarity form are stated here.

In §[\[stability_sect\]](#stability_sect){reference-type="ref" reference="stability_sect"}, we discuss some classical and some new polynomial stability theory results, and their multivariate analogues, in the homogeneous context. We also extend Laguerre's theorem to projectively convex regions (generalized circular regions), which later allows us to prove results regarding polynomials which have all their roots in a given interval.

In §[\[graces_sect\]](#graces_sect){reference-type="ref" reference="graces_sect"}, we state and prove our generalized Grace's theorem. We also discuss other stability regions to which the theorem applies, and consider symbols of linear operators given by evaluation at a particular point. We call these polynomials *evaluation symbols*, as they turn out to play a crucial role in the proofs of the operator characterizations.

In §[\[Cops_sect\]](#Cops_sect){reference-type="ref" reference="Cops_sect"}, we finally state and prove our improved characterizations of stability-preserving operators. We also demonstrate how the Borcea-Brändén characterizations can be seen (with a bit of work) to be corollaries of our characterizations. We then provide examples of the use of our results. In particular, we show how stability results related to classical polynomial convolutions can be immediately recovered.

In §[\[Rops_sect\]](#Rops_sect){reference-type="ref" reference="Rops_sect"}, we state and prove the analogous characterization of strong real stability-preserving operators. As with complex operators, we show how the Borcea-Brändén characterization can be obtained as a corollary. In this section, we also state and prove our characterization of operators which preserve both weak real-rootedness as well as interval- (or ray-) rootedness.

In Appendix [\[sl2_app\]](#sl2_app){reference-type="ref" reference="sl2_app"}, we explicate more of the representation theory of $SL_2(\mathbb{C})$ in a polynomial-minded way. Specifically, we prove a few standard tensor product decomposition results which more clearly demonstrate how this theory connects to the notion of apolarity.

In Appendix [\[gws_app\]](#gws_app){reference-type="ref" reference="gws_app"}, we discuss how polarization and the Grace-Walsh-Szegő coincidence theorem fit in to the framework presented in this paper. We also demonstrate that the classical isomorphism $V(n) \cong \operatorname{Sym}^n(V(1))$ (for representations of $\mathop{\mathrm{SL}}_2(\mathbb{C})$) can be realized as the polarization map and therefore has a stability-theoretic interpretation. While important to the conceptual thesis stated above, we place this discussion in an appendix as it is not utilized elsewhere.
