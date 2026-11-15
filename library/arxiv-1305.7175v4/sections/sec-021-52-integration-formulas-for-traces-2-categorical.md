---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-021-52-integration-formulas-for-traces-2-categorical
section_title: "Integration formulas for traces: 2-categorical consequences"
section_number: 5.2
pages: 31-33
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.904
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
[]{#2-cat label="2-cat"} Now we turn to the functoriality of dimensions and traces. For this we require the 2-categorical enhanced version $\uS$ of a sheaf theory, so as to take advantage of the resulting functorial adjunction $$\xymatrix{\cS(X) \ar@<+.5ex>[r]^{f_*} &
  \ar@<+.5ex>[l]^{f^!}\cS(Y)}$$ for $f:X\to Y$ proper. In particular, applying the functor $\uS$ on two-morphisms we find that

$\bullet$ A proper map $f:Z\to W$ of correspondences $$\xymatrix{
&\ar[dl]_-{p_Z} Z \ar[dd]^-f \ar[dr]^-{q_Z} & \\
X & & Y\\
& \ar[ul]^-{p_W} W\ar[ur]_-{q_W} & 
}$$ induces a canonical integration morphism of integral transforms $$\xymatrix{
\int_f: q_{Z*}p_Z^! \ar[r] & q_{W*} p_W^!
}$$

$\bullet$ In particular, when $X=Y=pt$, it induces a map of global volume forms $$\xymatrix{
\int_f: \omega(Z) \ar[r] & \omega(W)
}$$

$\bullet$ There is a canonical composition identity $$\xymatrix{
 \int_g\circ\int_{f}\simeq \int_{g\circ f}
 }$$

::: prop
[]{#sheaf unit and counit label="sheaf unit and counit"} For $f:X\to Y$ proper, the unit and counit of the $(f_*,f^!)$ adjunction are given respectively by integration along the proper maps of self-correspondences $\Delta_{/Y}:X\to X\times_Y X$ of $X$ and $f_{/Y}:X\to Y$ of $Y$: $$\xymatrix{
&\ar[dl]_-{} X \ar[dd]^-{\Delta_{f}} \ar[dr]^-{} & && &\ar[dl]_-{f} X \ar[dd]^-{f} \ar[dr]^-{f} & \\
X & & X  && Y & & Y\\
& \ar[ul]^-{p_1} X\times_Y X\ar[ur]_-{p_2} & && & \ar[ul]^-{} Y\ar[ur]_-{} & 
}$$
:::

::: proof
*Proof.* The assertion follows immediately from the geometric description of the unit and counit in the correspondence category, Proposition [\[geometric adjunction\]](#geometric adjunction){reference-type="ref" reference="geometric adjunction"}, upon applying the functor $\uS$. ◻
:::

::: prop
[]{#dim via integration label="dim via integration"} For any proper map $f:X\to Y$, the induced map on dimensions $$\xymatrix{
\dim(f_*):\dim(\cS(X))\ar[r] & \dim(\cS(Y))
}$$ is identified ($S^1$-equivariantly) with integration along the loop map $$\xymatrix{
\dim(f_*)\simeq \int_{\cL f}:\omega(\cL X) \ar[r] & \omega(\cL Y)
}$$
:::

::: proof
*Proof.* According to Definition [\[functorial dim\]](#functorial dim){reference-type="ref" reference="functorial dim"}, we must calculate the composition $$\xymatrix{
\dim(f_*):\Tr(\id_{\cS(X)})\ar[r]^-{\Tr(\eta_f)}& \Tr(f^!f_*) \ar[r]^-{\sim} & \Tr(f_*f^!) \ar[r]^-{\Tr(\epsilon_f)} & \Tr(\id_{\cS(Y)})
}$$ The equivalence of the middle arrow is given by the canonical identifications $$\Tr(f^!f_*)\simeq \omega((X\times_Y X) \times_{X \times X} X) \simeq \omega(X \times_{Y\times Y} Y) \simeq  \Tr(f_*f^!)$$

By Proposition [\[sheaf unit and counit\]](#sheaf unit and counit){reference-type="ref" reference="sheaf unit and counit"}, the unit $\eta_f:\id_{\cS(X)}\to f^! f_*$ is given by the integration morphism $$\xymatrix{\int_{\Delta_{f}}: \Delta_{f *}\omega_X \ar[r] & \omega_{X\times_Y X}
}$$ and hence its trace $\Tr(\eta_f):\Tr(\id_{\cS(X)})\to \Tr(f^! f_*)$ is given by the induced integration map $$\xymatrix{
\int_{\Delta_f}:\omega(\cL X)\ar[r] & \omega((X\times_Y X) \times_{X \times X} X)
}$$

Likewise, the counit $\epsilon_f:f_*f^!\to \id_{\cS(Y)}$ is given by by the integration morphism $$\xymatrix{
\int_f:f_*\omega_X\ar[r] & \omega_Y
}$$ and hence its trace $\Tr(\epsilon_f):\Tr(f_* f^!)\to Tr(\id_{\cS(Y)})$ is given by the induced integration map $$\xymatrix{
\int_{f}:\omega(X \times_{Y\times Y} Y )\ar[r] & \omega(\cL Y)
}$$

Finally, by functoriality, their composition is given by the integration map $$\xymatrix{
\int_{\cL f}:\omega(\cL X)\ar[r] & \omega(\cL Y)
}$$ ◻
:::

Finally, we have the functoriality of traces in parallel with the previous theorem on the functoriality of dimensions. Let us recall the relevant setup. Consider a proper morphism $f:X\to Y$ and endomorphisms $F_Z:X\to X$ and $F_W:Y\to Y$ in $Corr_k$ given by respective self-correspondences $X\leftarrow Z \to X$ and $Y \leftarrow W \to Y$.

By an $f$-morphism from the pair $(X,F_Z)$ to the pair $(Y,F_W)$, we mean an identification $$\xymatrix{
  s:Z  \ar[r]^-\sim &  X\times_Y W
  }$$ of correspondences from $X$ to $Y$. This in turn induces an identification of what might be called relative traces $$\xymatrix{
  Z\times_{Y\times Y} Y\ar[r]^-\sim &  X\times_{Y\times Y} W
  }$$ generalizing the relative loop space $\cL_X Y$ from the case of the identity correspondences $Z=X$, $W=Y$. We thus obtain a map of traces $$\xymatrix{
\tau(f, s):Z|_{\Delta_X}  =   Z\times_{X\times X} X \ar[r] &   Z \times_{Y\times Y} Y \ar[r]^-\sim &  X \times_{Y\times Y} W \ar[r] &  
  Y\times_{Y\times Y} W = W|_{\Delta_Y}
}$$

::: prop
[]{#trace via integration label="trace via integration"} With the preceding setup, the trace map $\Tr(f_*,s):\Tr(F_{X*})\to\Tr(F_{Y*})$ is canonically identified with the integration map $$\xymatrix{
\int_{\tau(f, s)} : \omega( Z|_{\Delta_X}) \ar[r] & \omega(W|_{\Delta_Y} )
}$$
:::

::: proof
*Proof.* The argument is parallel to the proof of Proposition [\[dim via integration\]](#dim via integration){reference-type="ref" reference="dim via integration"}. One calculates $\Tr(f_*,\alpha)$ from Definition [\[functorial trace\]](#functorial trace){reference-type="ref" reference="functorial trace"} using Proposition [\[geometric traces\]](#geometric traces){reference-type="ref" reference="geometric traces"} and the compatibility of Proposition [\[basic integral transforms\]](#basic integral transforms){reference-type="ref" reference="basic integral transforms"} and the integration morphism for integral transforms from Section [\[integration section\]](#integration section){reference-type="ref" reference="integration section"}. ◻
:::
