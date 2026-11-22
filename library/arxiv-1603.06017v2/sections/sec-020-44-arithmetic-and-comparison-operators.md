---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-020-44-arithmetic-and-comparison-operators
section_title: "Arithmetic and Comparison Operators"
section_number: 4.4
pages: 16-17
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.927
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:arithmetic and comparison}
Recall that for every number system $\mathbf{S}$ that we use in Walnut
the three automata $(a,b,c):\text{?S }a=b+c$, $(a,b): \text{?S
}a=b$\footnote{This automaton does not need to be defined explicitly by
the user, because we assumed for all number systems $\mathbf{S}$ in
Walnut $a=_{\mathbf{S}}b$ if and only if $a=b$.}, and $(a,b):\text{?S
}a<b$ are defined. In this section we show that using these three
automata and the decision procedure outlined in Sections \ref{sec:cross
product}--\ref{sec:complement and reverse}, we can construct automata
for more complex relative expressions with lots of arithmetic
operators.

For a constant $c>0$, a natural number, automata $(a):\text{?S }a=c$
can be constructed recursively using automata $(b):\text{?S }b=c'$ and
$(a,b):\text{?S }a=b+1$ where $c'$ is the predecessor of $c$, i.e.,
$c'+1=c$. For example, predicate $\text{?S }a=2$ is equivalent to
$\text{?S }\text{E}b\text{ }a=b+1 \mathbin{\&} b=1.$ Similarly
$\text{?S }b=1$ is equivalent to $\text{?S }\text{E}b_2\text{ } b=b_2+1
\mathbin{\&} b_2=0$. Based on Definition \ref{def:number systems}, for
all number systems $\mathbf{S}$, the automaton for $\text{?S }b_2=0$ is
the simple automaton accepting $0^*$. To construct automaton $(a,b):
\text{?S }a=b+1$, just note that the predicate is equivalent to
$\text{?S }\text{E}c\text{ } a=b+c \mathbin{\&} c=1$.

A similar recursive argument can be applied to obtain $(a,b): a=c*b$
for a constant $c>0$, i.e.,  one can construct $(a,b): (a=b_2+b)
\mathbin{\&} (b_2=c'*b)$ where $c'$ is the predecessor of $c$. The
similar argument can be applied to obtain automata for division by
constants or subtraction.

To construct $(a,b): \text{?S }a<=b$, note its equivalence to $(a,b):
\text{?S }a<b \mid a=b$. With similar arguments, one can construct
automaton for other comparison operators.

It is important to understand Walnut's construction of
$$(y,x_1,x_2,\ldots,x_n):\text{?S } y \olessthan (x_1 \otimes_1 x_2
\otimes_2 \cdots \otimes_{n-1} x_n)$$ where $n\geq 3$. Here
$\olessthan$ denotes an arbitrary comparison operator, and the
$\otimes_i$ are arbitrary arithmetic operators. Also let $y$ and
$x_i$ be variables or arithmetic constants. All arithmetic operators
in Walnut are associative from left to right; see Section
\ref{sec:operators}. Based on this, Walnut first transforms the
predicate to an equivalent predicate $$(y,x_1,x_2,\ldots,x_n):\text{?S
E}y_1,\ldots,y_{n-2}\text{ } (y_1=x_1 \otimes_1
x_2)\mathbin{\&}(y_2=y_1\otimes_2 x_3) \mathbin{\&}\cdots\mathbin{\&}
(y=y_{n-2}\otimes_{n-1} x_n).$$ Now Walnut has all the resources
necessary to construct this last automaton.

For example, to construct $(a): 0\text{<=}(a-1+1)$, Walnut first transforms it to $(a): \text{E}b\text{ }(b=a-1)\mathbin{\&}(0=b+1)$. The automaton is depicted below:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{negative}
	\caption{Automaton for $0\text{<=}a-1+1$ does not accept $0^*$}
	\label{fig:negative}
\end{figure}
There is something here that is worth noting. Note how this automaton
does not accept $0$? In arithmetic over integers $a=0$ satisfies the
predicate. However in Presburger arithmetic setting $a=0$ gives $b=-1$,
which is not acceptable, since Presburger arithmetic is defined over
natural numbers. In order to fix this issue, try to always postpone
subtraction and division to the rightmost position in your predicates.
For example, writing $(a): 0<=(a+1-1)$ results in
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{negative_fixed}
	\caption{Automata for $0\text{<=}a+1-1$ accepts $0^*$}
	\label{fig:negative_fixed}
\end{figure}
