---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-007-32-symmetry
section_title: "Symmetry."
section_number: 3.2
pages: 16-17
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.sym label="sec.sym"} As a final step we consider the symmetry structure. This is an essential ingredient at the level of duality theory ([@DR89 §1]) and, at the same time, encodes the Fermi-Bose statistics (see [@Dop11] for a friendly introduction). We introduce the family of unitary operators

$$\label{eq.sym.z1}
\epsilon(z_\rho,w_\sigma)_e := w_\sigma(p_{oe})^* \sigma_o(z_\rho(p_{o'e}))^* \cdot
                            z_\rho(p_{o'e}) \rho_e(w_\sigma(p_{oe}))
\ \ , \ \
\forall  e < a
\ ,$$

where

$p_{oe} : e \to o$, $p_{o'e} : e \to o'$ are paths in $\Delta^a$ such that $o \perp o'$.

The fact the for any $a \in \Delta$ there are causally disjoint $o,o' < a$ is an immediate consequence of [@BR08 Lemma B.5], so any $\epsilon(z_\rho,w_\sigma)_e$, $e < a$, is well-defined as an element of $UH \cap R_a$.

By Lemma [\[lem.qft2\]](#lem.qft2){reference-type="ref" reference="lem.qft2"} we have that $\epsilon(z_\rho,w_\sigma)_e$ is independent of the choice of $p_{oe}$, $p_{o'e}$, $o$ and $o'$.

The family $\epsilon(z_\rho,w_\sigma)$ fulfils the symmetry relations of [@DR89 §1], which, in our setting, take the form

$$\label{eq.sym}
\left\{
\begin{array}{ll}
\epsilon(z_\rho,w_\sigma)_{\partial_0 b}\cdot (z \otimes w)_{\rho \circ \sigma}(b) 
\ = \
(w \otimes z)_{\sigma \circ \rho}(b) \cdot \epsilon(z_\rho,w_\sigma)_{\partial_1 b}\ ,

\\

(s \otimes t)_e \cdot \epsilon(z_\rho,w_\sigma)_e 
\ = \
\epsilon(z'_{\rho'},w'_{\sigma'})_e \cdot (t \otimes s)_e \ ,

\\

\epsilon(z_\rho,w_\sigma)_e \cdot \epsilon(w_\sigma,z_\rho)_e \ = \ 1
\ \ \ , \ \ \
\epsilon(\iota^a,z_\rho)_e \ = \ \epsilon(z_\rho,\iota^a)_e = 1 \ ,
\\
\epsilon(  (z \otimes w)_{\rho \circ \sigma} , v_\tau  )_e
\ = \
\epsilon(z_\rho,v_\tau)_e \cdot \rho_e (\epsilon(w_\sigma,v_\tau)_e)
\ ,

\end{array}
\right.$$

$\forall e < a$, $z_\rho,z'_{\rho'}, w_\sigma,w'_{\sigma'} ,v_\tau \in {\bf obj \ }Z^1_c(\EuFrak{R})_{< a}$, $t \in (z_\rho,z'_{\rho'})$, $s \in (w_\sigma,w'_{\sigma'})$, $b \in \Sigma_1(\Delta^a)$.

The explicit computations, that are on the line of [@Rob; @Ruz05; @BR08], are postponed in §[\[app.sym\]](#app.sym){reference-type="ref" reference="app.sym"}. It is at this point that we make use of the fact that we must have $s \geq 2$ spatial dimensions, as otherwise we may get a braiding instead of a symmetry. Since, as mentioned in the Introduction, where are interested in ordinary Bose-Fermi statistics, in the rest of the section we shall assume that $M$ has spacetime dimension $\geq 3$.

Now, even if ([\[eq.sym\]](#eq.sym){reference-type="ref" reference="eq.sym"}) are fulfilled, in general

$\epsilon(z_\rho,w_\sigma)$

*does not* define a symmetry, because we should have

$$\epsilon(z_\rho,w_\sigma)_e \in R_e \ \ , \ \ \forall e < a \ .$$

The standard way to prove the above property would be the following. In general, if $t \in (\rho_e,\sigma_e)$ then

$$t t' = t \rho_e(t') = \sigma_e(t') t = t't \ , \  \forall o \perp e , t' \in R_o
\ \Rightarrow \ 
t \in R_o' \ , \ \forall o \perp e \ ,$$

and this, by (punctured) Haag duality, suffices to conclude that $t \in R_e$. In particular, in our case we can verify that

$\epsilon(z_\rho,w_\sigma)_e \in ( \sigma_e \rho_e , \rho_e \sigma_e )$,

nevertheless we are working with families of operators in the restricted net

$$\EuFrak{R}|_{\Delta^a} \ = \ (  \{ R_e \}_{e<a} \ , \jmath )_{\Delta^a} \ ,$$

that could violate punctured Haag duality because, given $x \in M$, we expect that the inclusion

$$R_e   \ =  \ \cap_{o \perp e , \overline o \perp \{ x \} } R_o' 
\ \ \subseteq \ \
R^a_e \ := \ \cap_{o \perp e , o < a} R_o'$$

is proper for any $e < a$. Thus we can conclude only that

$\epsilon(z_\rho,w_\sigma)_e \in R^a_e$, $e < a$.

In the next subsection we show how to avoid this difficulty using Rem.[\[rem.back1\]](#rem.back1){reference-type="ref" reference="rem.back1"}.
