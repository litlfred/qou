---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-057-theoretical-foundation
section_title: "Theoretical foundation"
section_number: null
pages: 137-139
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
We use an analytical function ΨT(x) as the importance sampling function for the
N-particle system. We deﬁne a new distribution function f(x, τ),
f(x, τ) ≡ΨT(x)φ(x, τ).
(B.25)
The key is, we want to ﬁnd the short-time Green’s function for the distribution f(x, τ),
such that after many time steps, the distribution will evolve into ΨTΨ0(not Ψ0), which
will be convenient for further calculations.
By multiplying ΨT(x) to both sides of Eq.(B.13), we have Fokker-Planck equation,
∂f
∂τ = DΨT∇2φ + [ET −V (x)]f
=

D∇2f −D
N
X
i=1
∇i · (fFiQ)

|
{z
}
drifting
+ [ET −EL(x)]f
|
{z
}
branching
,
(B.26)
127
where ∇2 ≡PN
i=1 ∇2
i , and the local energy is deﬁned as EL(x) ≡HΨT
ΨT . In particular,
the so called quantum force for particle i is deﬁned as
FiQ ≡2∇iΨT
ΨT
.
(B.27)
We notice that by using the property ∇· (fF ) = (F · ∇+ ∇· F )f, the drifting part
in the right-hand side (RHS) of Eq.(B.26) can be rewritten as
D∇2f −
N
X
i=1
D(FiQ · ∇i + ∇i · FiQ)f ≡−˜Jf,
(B.28)
where
˜J ≡−D∇2 +
N
X
i=1
D(FiQ · ∇i + ∇i · FiQ)
(B.29)
is the modiﬁed kinetic energy operator. So, Eq.(B.26) can be further written as
∂f
∂τ =
n
−˜J + [ET −EL(x)]
o
f,
(B.30)
which means the short-time evolution operator is just e{−˜J+[ET −EL(x)]}τ. Consider that
τ is very small, we further have e{−˜J+[ET −EL(x)]}τ ≈e−˜Jτe[ET −EL(x)]τ. Therefore
f(x, t + τ) = e−˜Jτe[ET −EL(x)]τf(x, t) = e−˜Jτf(x, t)e[ET −EL(x)]τ.
(B.31)
By sandwiching Eq.(B.31) between ⟨y| and |x⟩, we have
⟨y|f(x, t + τ)|x⟩=
Z
dx′⟨y|e−˜Jτ|x′⟩⟨x′|f(x, t)|x⟩e[ET −EL(x)]τ
⇒f(x, t + τ)δ(y −x) =
Z
dx′⟨y|e−˜Jτ|x′⟩f(x, t)δ(x −x′)e[ET −EL(x)]τ.
(B.32)
By doing integral over x on both sides of Eq.(B.32) we have
Z
f(x, t + τ)δ(y −x)dx =
Z
dx′
Z
dx⟨y|e−˜Jτ|x′⟩f(x, t)δ(x −x′)e[ET −EL(x)]τ
⇒f(y, t + τ) =
Z
dx ⟨y|e−˜Jτ|x⟩
|
{z
}
˜Gdiﬀ(y,x,τ)
f(x, t) e[ET −EL(x)]τ
|
{z
}
˜GB(y,x,τ)
.
(B.33)
˜Gdiﬀ(y, x, τ) satisﬁes the diﬀusion equation ∂˜Gdiﬀ(y,x,τ)
∂τ
= −˜J ˜Gdiﬀ(y, x, τ), which
means that if we set the branch part as zero, the distribution f(x, τ) will evolve into
128
Ψ2
T(x), and ⟨EL⟩will just be variational energy. Assuming the quantum force FiQ(x)
is constant between x and y, the solution is
˜Gdiﬀ(y, x, τ) = (4πDτ)−3N
2
N
Y
i=1
e−
|yi−xi−DτFiQ(x)|2
4Dτ
≡
N
Y
i=1
˜G(i)
diﬀ(yi, xi, τ),
(B.34)
note that
R ˜Gdiﬀ(y, x, τ)dx = 1 which is a Gaussian integral. So, ˜Gdiﬀ(y, x, τ) can be
treat as a probability density.
The branch part ˜GB(x, τ) = e−[EL(x)−ET ]τ is usually written symmetrically (Ham-
mond et al. (1994); Kalos and Whitlock (2008)) as
˜GB(y, x, τ) = e−[ EL(x)+EL(y)
2
−ET ]τ.
(B.35)
Now the short-time approximated Green’s function for f can be written as
˜G(y, x, τ) = ˜Gdiﬀ(y, x, τ) ˜GB(y, x, τ),
(B.36)
such that,
f(y, t + τ) =
Z
˜G(y, x; τ)f(x, t)dx =
Z
˜Gdiﬀ(y, x, τ) ˜GB(y, x, τ)f(x, t)dx. (B.37)
Similar with the non-importance sampling DMC, Eq.(B.26) is the combination
of drifting and branching terms. The entire simulation can be achieved by drifting
and branching process described in Sec.B, just use the modiﬁed Green’s function
instead. Finally f will converge to ΨTΨ0. This is because that we are actually still
solving Eq.(B.13), but just by using Eq.(B.26). The φ in Eq.(B.13) converges to Ψ0,
which exactly means that solution of Eq.(B.26) will converge to ΨTΨ0. Moreover, if
we neglect the branch part, the diﬀusion process will evolve the distribution into Ψ2
T,
and DMC then just becomes VMC.
