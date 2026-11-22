---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-006-3-turaevs-notion-of-modular-category
section_title: "Turaev's notion of modular category"
section_number: 3
pages: 5-7
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.974
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:T-mod_cat}

Using the language of \cite{EGNO15}, a \textit{T-modular category} (T for Turaev) is a ribbon fusion category whose S-matrix is invertible. The definition originally appeared in \cite[Sec.~II.1.2]{T94} in a slightly more general form, but the version reported here has since become rather standard (compare with \cite{BK01,TV17}). In order to better grasp this notion, let us proceed to unpack the terminology. 

First of all, a \textit{ribbon} category $\calC$ is a braided rigid monoidal category with a twist. This means a ribbon category comes equipped with:
\begin{enumerate}
 \item a tensor product $\otimes : \calC \times \calC \to \calC$ and a tensor unit $\one \in \calC$;
 \item duality morphisms $\lev_X : X^* \otimes X \to \one$, $\lcoev_X : \one \to X \otimes X^*$, and $\rev_X : X \otimes X^* \to \one$, $\rcoev_X : \one \to X^* \otimes X$ for every $X \in \calC$;
 \item braiding morphisms $c_{X,Y} : X \otimes Y \to Y \otimes X$ for all $X,Y \in \calC$;
 \item twist morphisms $\theta_X : X \to X$ for every $X \in \calC$.
\end{enumerate}
All these structure data are subject to several axioms, which can be found explicilty in \cite[Sec.~2.1, 2.10, 8.1, 8.10]{EGNO15}, but which can also be understood efficiently using a more visual approach. Indeed, morphisms of a ribbon category can be represented using an extension of \textit{Penrose graphical notation} and \textit{string diagrams}. Structure morphisms listed above are represented by elementary diagrams
\begin{align*}
 \id_X &= \pic{graphical_rep_id} &
 \id_{X^*} &= \pic{graphical_rep_id_dual} \\[2pt]
 \lev_X &= \pic{graphical_rep_lev} &
 \lcoev_X &= \pic{graphical_rep_lcoev} \\[2pt]
 \rev_X &= \pic{graphical_rep_rev} &
 \rcoev_X &= \pic{graphical_rep_rcoev} \\[2pt]
 c_{X,Y} &= \pic{graphical_rep_braiding} &
 \theta_X &= \pic{graphical_rep_twist}
\end{align*}
In general, a morphism $f : X_1 \otimes \ldots \otimes X_m \to Y_1 \otimes \ldots \otimes Y_n$ which is not expressed as a combination of structure morphisms is simply placed inside a box 
\begin{equation}\label{E:coupon}
 f = \pic{graphical_rep_coupon}
\end{equation}
These diagrams are read from bottom to top.\footnote{Remark that the convention used here for orientations is opposite to the one used by Turaev, but also widely used.} Composition is given by vertical stacking, while tensor product corresponds to horizontal juxtaposition. Then, the axioms of a ribbon category translate precisely to the invariance of this diagrammatic calculus under isotopy and framed Reidemeister moves.

Next, let us fix an algebraically closed\footnote{This condition is not necessary, but convenient.} field $\Bbbk$. Throughout this paper, we will use the term ``linear'' as a shorthand for ``$\Bbbk$-linear''. Then, let us consider a linear category $\calC$, which is a category whose sets of morphisms carry vector space structures making compositions into bilinear maps. We say that $\calC$ is \textit{finite} if it is equivalent to the category of finite-dimensional representations of a finite-dimensional algebra. This definition is rather implicit, as no algebra is attached to $\calC$, but it can be reformulated in more explicit terms. In fact, as explained in \cite[Def.~1.8.6]{EGNO15}, $\calC$ is finite if and only if it is abelian and:
\begin{enumerate}
 \item it has a finite number of isomorphism classes of simple objects;
 \item it has enough projectives;
 \item its objects have finite lenght; 
 \item its morphism spaces have finite dimension.
\end{enumerate}
A \textit{fusion category} is a finite semisimple monoidal linear category. Therefore, it is this assumption that encodes the semisimplicity of T-modular categories. 

Finally, for every ribbon fusion category we can define an \textit{S-matrix} given by 
\[
 S(\calC) := \left( \pic{S-matrix} \right)_{i,j \in I}
\]
where $\Gamma(\calC) = \left\{ V_i \mid i \in I \right\}$ is a set of representatives of isomorphism classes of simple objects of $\calC$. We say a ribbon fusion category $\calC$ is T-modular if $S(\calC)$ is invertible. This requirement can be understood as a non-degeneracy condition for the braiding of a ribbon fusion category.

We finish this section with an additional definition. The \textit{Müger center} $M(\calC)$ of a ribbon category $\calC$ is the full subcategory of so-called \textit{transparent} objects of $\calC$, that is, $X \in M(\calC)$ if $c_{Y,X} \circ c_{X,Y} = \id_{X \otimes Y}$ for every $Y \in \calC$. The Müger center of a ribbon category $\calC$ is said to be trivial if every transparent object of $\calC$ is isomorphic to a direct sum of copies of the tensor unit $\one$. Then, a ribbon fusion category $\calC$ has trivial Müger center if and only if $S(\calC)$ is invertible \cite[Prop.~1.1]{B00}. This equivalent non-degeneracy condition for the braiding of $\calC$ will be useful later on.
