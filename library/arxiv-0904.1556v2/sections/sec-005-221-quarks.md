---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-005-221-quarks
section_title: "Quarks"
section_number: 2.2.1
pages: 13-17
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:quarks label="sec:quarks"}

In the last section, we learned how Heisenberg unified the proton and neutron into the nucleon, and that Yukawa proposed that nucleons interact by exchanging pions. This viewpoint turned out to be at least approximately true, but it was based on the idea that the proton, neutron and pions were all fundamental particles without internal structure, which was not ultimately supported by the evidence.

Protons and neutrons are not fundamental. They are made of particles called **quarks**. There are a number of different types of quarks, called **flavors**. However, it takes only two flavors to make protons and neutrons: the **up quark**, $u$, and the **down quark**, $d$. The proton consists of two up quarks and one down: $$p = uud$$ while the neutron consists of one up quark and two down: $$n = udd$$ Protons have an electric charge of $+1$, exactly opposite the electron, while neutrons are neutral, with $0$ charge. These two conditions are enough to determine the charge of their constituents, which are fundamental fermions much like the electron: 1em

::: center
  **Fundamental Fermions (second try)**                                
  --------------------------------------- ----------- ---------------- --
  Name                                      Symbol         Charge      
  Electron                                   $e^-$          $-1$       
                                                                       
  Up quark                                 $u \quad$   $+\frac{2}{3}$  
                                                                       
  Down quark                               $d \quad$   $-\frac{1}{3}$  
:::

1em There are more quarks than these, but these are the lightest ones, comprising the **first generation**. They are all we need to make protons and neutrons, and so, with the electron in tow, the above list contains all the particles we need to make atoms.

Yet quarks, fundamental as they are, are never seen in isolation. They are always bunched up into particles like the proton and neutron. This phenomenon is called **confinement**. It makes the long, convoluted history of how we came to understand quarks, despite the fact that they are never seen, all the more fascinating. Unfortunately, we do not have space for this history here, but it can be found in the books by Crease and Mann [@CreaseMann:sc], Segrè [@segre:modern], and Pais [@pais:ib].

It is especially impressive how physicists were able to discover that each flavor of quark comes in three different states, called **colors**: **red** $r$, **green** $g$, and **blue** $b$. These 'colors' have nothing to do with actual colors; they are just cute names---though as we shall see, the names are quite well chosen. Mathematically, all that matters is that the Hilbert space for a single quark is ${\mathbb C}^3$; we call the standard basis vectors $r, g$ and $b$. The **color symmetry group** ${\rm SU}(3)$ acts on this Hilbert space in the obvious way, via its fundamental representation.

Since both up and down quarks come in three color states, there are really six kinds of quarks in the matter we see around us. Three up quarks, spanning a copy of ${\mathbb C}^3$: $$u^r, u^g, u^b \in {\mathbb C}^3 .$$ and three down quarks, spanning another copy of ${\mathbb C}^3$: $$d^r, d^g, d^b \in {\mathbb C}^3 .$$ The group ${\rm SU}(3)$ acts on each space. All six quarks taken together span this vector space: $${\mathbb C}^3 \oplus {\mathbb C}^3 \cong{\mathbb C}^2 \otimes {\mathbb C}^3$$ where ${\mathbb C}^2$ is spanned by the flavors $u$ and $d$. Put another way, a first-generation quark comes in one of six flavor-color states.

How could physicists discover the concept of color, given that quarks are confined? In fact confinement was the key to this discovery! Confinement amounts to the following decree: all observed states must be **white**, i.e., invariant under the action of ${\rm SU}(3)$. It turns out that this has many consequences.

For starters, this decree implies that we cannot see an individual quark, because they all transform nontrivially under ${\rm SU}(3)$. Nor do we ever see a particle built from two quarks, since no unit vectors in ${\mathbb C}^3 \otimes {\mathbb C}^3$ are fixed by ${\rm SU}(3)$. But we *do* see particles made of three quarks: namely, nucleons! This is because there *are* unit vectors in $${\mathbb C}^3 \otimes {\mathbb C}^3 \otimes {\mathbb C}^3$$ fixed by ${\rm SU}(3)$. Indeed, as a representation of ${\rm SU}(3)$, ${\mathbb C}^3 \otimes {\mathbb C}^3 \otimes {\mathbb C}^3$ contains precisely one copy of the trivial representation: the antisymmetric rank three tensors, $\Lambda^3 {\mathbb C}^3 \subseteq
{\mathbb C}^3 \otimes {\mathbb C}^3 \otimes {\mathbb C}^3$. This one dimensional vector space is spanned by the wedge product of all three basis vectors: $$r \wedge b \wedge g \in \Lambda^3 {\mathbb C}^3.$$ So, up to normalization, this *must* be the color state of a nucleon. And now we see why the 'color' terminology is well-chosen: an equal mixture of red, green and blue light is white. This is just a coincidence, but it is too cute to resist.

So: color is deeply related to confinement. Flavor, on the other hand, is deeply related to isospin. Indeed, the flavor ${\mathbb C}^2$ is suspiciously like the isospin ${\mathbb C}^2$ of the nucleon. We even call the quark flavors 'up' and 'down'. This is no accident. The proton and neutron, which are the two isospin states of the nucleon, differ only by their flavors, and only the flavor of one quark at that. If one could interchange $u$ and $d$, one could interchange protons and neutrons.

Indeed, we can use quarks to explain the isospin symmetry of Section [\[sec:isospin\]](#sec:isospin){reference-type="ref" reference="sec:isospin"}. Protons and neutrons are so similar, with nearly the same mass and strong interactions, because $u$ and $d$ quarks are so similar, with nearly the same mass and truly identical colors.

So as in Section [\[sec:isospin\]](#sec:isospin){reference-type="ref" reference="sec:isospin"}, let ${\rm SU}(2)$ act on the flavor states ${\mathbb C}^2$. By analogy with that section, we call this ${\rm SU}(2)$ the isospin symmetries of the quark model. Unlike the color symmetries ${\rm SU}(3)$, these symmetries are not exact, because $u$ and $d$ quarks have different mass and charge. Nevertheless, they are useful.

The isospin of the proton and neutron then arises from the isospin of its quarks. Define $I_3(u) = \frac{1}{2}$ and $I_3(d) = -\frac{1}{2}$, making $u$ and $d$ the isospin up and down states at which their names hint. To find the $I_3$ of a composite, like a proton or neutron, add the $I_3$ for its constituents. This gives the proton and neutron the right $I_3$: $$\begin{array}{ccccr}
    I_3( p ) & = & \frac{1}{2}+ \frac{1}{2}- \frac{1}{2}&=& \frac{1}{2}\\
                                                       \\
    I_3( n ) & = & \frac{1}{2}- \frac{1}{2}- \frac{1}{2}&=& -\frac{1}{2}. \\
\end{array}$$ Of course, having the right $I_3$ is not the whole story for isospin. The states $p$ and $n$ must still span a copy of the fundamental rep ${\mathbb C}^2$ of ${\rm SU}(2)$. Whether or not this happens depends on how the constituent quark flavors transform under ${\rm SU}(2)$.

The states $u \otimes u \otimes d$ and $u \otimes d \otimes d$ do *not* span a copy of the fundamental rep of ${\rm SU}(2)$ inside ${\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2$. So, as with color, the equations $$p = uud, \quad n = udd$$ fail to give us the whole story. For the proton, we actually need some linear combination of the $I_3 = \frac{1}{2}$ flavor states, which are made of two $u$'s and one $d$: $$u \otimes u \otimes d, \quad u \otimes d \otimes u, \quad d \otimes u \otimes u  \quad \in \quad {\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2.$$ And for the neutron, we need some linear combination of the $I_3 = -\frac{1}{2}$ flavor states, which are made of one $u$ and two $d$'s: $$u \otimes d \otimes d, \quad d \otimes u \otimes d, \quad d \otimes d \otimes u  \quad \in \quad {\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2.$$ Writing $p = uud$ and $n = udd$ is just a sort of shorthand for saying that $p$ and $n$ are made from basis vectors with those quarks in them.

In physics, the linear combination required to make $p$ and $n$ work also involves the 'spin' of the quarks, which lies outside of our scope. We will content ourselves with showing that it *can* be done. That is, we will show that ${\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2$ really does contain a copy of the fundamental rep ${\mathbb C}^2$ of ${\rm SU}(2)$. To do this, we use the fact that any rank 2 tensor can be decomposed into symmetric and antisymmetric parts; for example, $${\mathbb C}^2 \otimes {\mathbb C}^2 \cong{\rm Sym}^2 {\mathbb C}^2 \oplus \Lambda^2 {\mathbb C}^2$$ and this is actually how ${\mathbb C}^2 \otimes {\mathbb C}^2$ decomposes into irreps. ${\rm Sym}^2
{\mathbb C}^2$, as we noted in Section [\[sec:isospin\]](#sec:isospin){reference-type="ref" reference="sec:isospin"}, is the unique 3-dimensional irrep of ${\rm SU}(2)$; its othogonal complement $\Lambda^2 {\mathbb C}^2$ in ${\mathbb C}^2 \otimes {\mathbb C}^2$ is thus also a subrepresentation, but this space is 1-dimensional, and must therefore be the trivial irrep, $\Lambda^2 {\mathbb C}^2 \cong{\mathbb C}$. In fact, for any ${\rm SU}(n)$, the top exterior power of its fundamental rep, $\Lambda^n {\mathbb C}^n$, is trivial.

As a representation of ${\rm SU}(2)$, we thus have $$\begin{aligned}
    {\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2 
               & \cong& {\mathbb C}^2 \otimes ( {\rm Sym}^2 {\mathbb C}^2 \oplus {\mathbb C}) \\
               & \cong& {\mathbb C}^2 \otimes {\rm Sym}^2 {\mathbb C}^2 \quad \oplus \quad {\mathbb C}^2. 
\end{aligned}$$ So indeed, ${\mathbb C}^2$ is a subrepresentation of ${\mathbb C}^2 \otimes {\mathbb C}^2 \otimes {\mathbb C}^2$.

As in the last section, there is no reason to have the full ${\mathbb C}^2$ of isospin states for nucleons unless there is a way to change protons into neutrons. There, we discussed how the pions provide this mechanism. The pions live in $\mathfrak{sl}(2, {\mathbb C})$, the complexification of the adjoint representation of ${\rm SU}(2)$, and this acts on ${\mathbb C}^2$: 1em

::: center
![image](piN_vertex)
:::

1em This Feynman diagram is a picture of the intertwining operator $\mathfrak{sl}(2, {\mathbb C})
\otimes {\mathbb C}^2 \to {\mathbb C}^2$ given by the representation of $\mathfrak{sl}(2, {\mathbb C})$ on ${\mathbb C}^2$. Now we know that nucleons are made of quarks and that isospin symmetry comes from their flavor symmetry. What about pions?

Pions also fit into this model, but they require more explanation, because they are made of quarks and 'antiquarks'. To every kind of particle, there is a corresponding antiparticle, which is just like the original particle but with opposite charge and isospin. The antiparticle of a quark is called an **antiquark**.

In terms of group representations, passing from a particle to its antiparticle corresponds to taking the dual representation. Since the quarks live in ${\mathbb C}^2 \otimes {\mathbb C}^3$, a representation of ${\rm SU}(2) \times {\rm SU}(3)$, the antiquarks live in the dual representation ${\mathbb C}^{2*} \otimes {\mathbb C}^{3*}$. Since ${\mathbb C}^2$ has basis vectors called **up** and **down**: $$u = \left( \begin{array}{c} 1 \\ 0 \end{array} \right) \in {\mathbb C}^2  \qquad
d = \left( \begin{array}{c} 0 \\ 1 \end{array} \right) \in {\mathbb C}^2$$ the space ${\mathbb C}^{2*}$ has a dual basis $$\overline{u}= \left( 1, 0 \right) \in {\mathbb C}^{2*}  \qquad
        \overline{d}= \left( 0, 1 \right) \in {\mathbb C}^{2*}$$ called **antiup** and **antidown**. Similarly, since the standard basis vectors for ${\mathbb C}^3$ are called red, green and blue, the dual basis vectors for ${\mathbb C}^{3*}$ are known as **anticolors**: namely **antired** ${\overline{r}}$, **antigreen** ${\overline{g}}$, and **antiblue** ${\overline{b}}$. When it comes to actual colors of light, antired is called 'cyan': this is the color of light which blended with red gives white. Similarly, antigreen is magenta, and antiblue is yellow. But few physicists dare speak of 'magenta antiquarks'---apparently this would be taking the joke too far.

All pions are made from one quark and one antiquark. The flavor state of the pions must therefore live in $${\mathbb C}^2 \otimes {\mathbb C}^{2*}.$$ We can use the fact that pions live in $\mathfrak{sl}(2, {\mathbb C})$ to find out how they decompose into quarks and antiquarks, since $$\mathfrak{sl}(2, {\mathbb C}) \subseteq {\rm End}({\mathbb C}^2).$$ First, express the pions as matrices: $$\pi^+ = \left(\begin{array}{cc} 0 & 1 \\ 0 & 0 \end{array} \right) \quad  
\pi^0 = \left(\begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array} \right) \quad
\pi^- = \left(\begin{array}{cc} 0 & 0 \\ 1 & 0 \end{array} \right) .$$ We know they have to be these matrices, up to normalization, because these act the right way on nucleons in ${\mathbb C}^2$: $$\pi^- + p \to n$$ $$\pi^+ + n \to p$$ $$\pi^0 + p \to p$$ $$\pi^0 + n \to n .$$ Now, apply the standard isomorphism ${\rm End}({\mathbb C}^2) \cong{\mathbb C}^2 \otimes {\mathbb C}^{2*}$ to write these matrices as linear combinations of quarks and antiquarks: $$\pi^+ = u \otimes \overline{d}, \quad \pi^0 = u \otimes \overline{u}- d \otimes \overline{d}, \quad \pi^- = d \otimes \overline{u}.$$ Note these all have the right $I_3$, because isospins reverse for antiparticles. For example, $I_3(\overline{d}) = +\frac{1}{2}$, so $I_3(\pi^+) = 1$.

In writing these pions as quarks and antiquarks, we have once again neglected to write the color, because this works the same way for all pions. As far as color goes, pions live in $${\mathbb C}^3 \otimes {\mathbb C}^{3*}.$$ Confinement says that pions need to be white, just like nucleons, and there is only a one-dimensional subspace of ${\mathbb C}^3 \otimes {\mathbb C}^{3*}$ on which ${\rm SU}(3)$ acts trivially, spanned by $$r \otimes {\overline{r}}+ 
g \otimes {\overline{g}}+ b \otimes {\overline{b}}\in {\mathbb C}^3 \otimes {\mathbb C}^{3*} .$$ So, this must be the color state of all pions.

Finally, the Gell-Mann--Nishijima formula also still works for quarks, provided we define the hypercharge for both quarks to be $Y = \frac{1}{3}$: $$\begin{array}{ccccrcr}
    Q(u) &=& I_3(u) + Y/2 & = & \frac{1}{2}+ \frac{1}{6}  &=& \frac{2}{3}\\
                                                                        \\
    Q(d) &=& I_3(d) + Y/2 & = & -\frac{1}{2}+ \frac{1}{6} &=& -\frac{1}{3}.  
\end{array}$$ Since nucleons are made of three quarks, their total hypercharge is $Y = 1$, just as before.
