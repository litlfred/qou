---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-011-41-explicit-assignment-of-octonion-units-to-sta
section_title: "Explicit assignment of octonion units to STA elements"
section_number: 4.1
pages: 9-12
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.881
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
We now discuss the explicit linking of the octonion units $e_0$ through $e_7$ with the 8 elements making up Dirac spinors in the STA. The latter are the even elements of the STA, which as mentioned above, can be derived as the full geometric algebra of 3d space, via the identification $\sigma_i = \gamma_i \gamma_0$, $i=1,2,3$, as illustrated in Fig.~\ref{fig:sta-split}.

\begin{figure}
\begin{center}    
\includegraphics[width=0.7\textwidth]{sta_split.jpg}
\caption{Illustration of the relation between the even elements of the STA (blue entries on the top line) and the full 3d Pauli algebra (the geometric algebra of 3d space, bottom line).}
\label{fig:sta-split}
\end{center}
\end{figure}

Note also that this identification enables the use of the same pseudoscalar $I$ in the 4d and 3d spaces, since

\be
I=\go\gam_1\gam_2\gam_3=\sigma_1\sigma_2\sigma_3
\ee


It is fairly obvious that we will wish to associate the octonion unit $e_0$ with the scalar `1', but what about the remaining 7 entries? This depends on the multiplication table for the octonions we want to achieve, and even then there are a variety of options.

As a first example, we could aim to match the multiplication table as first given (in implied form) in the first publication concerning Octonions, i.e.\ the 1845 paper by Cayley\cite{cayley1845xxviii}. (It may be worth noting that in fact this paper was about the quite different subject of Elliptic Functions, with the Octonions occupying only a postscript. Similarly the paper by Graves, which appeared shortly afterwards\cite{graves1845xlvi}, concerned objects he had introduced called `couples', with again the Octonions only mentioned in a postscript!)

This multiplication table (the original Cayley one) is shown in Table~\ref{table:cayley-mult}

\begin{table}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline & $e_{0}$ & $e_{1}$ & $e_{2}$ & $e_{3}$ & $e_{4}$ & $e_{5}$ & $e_{6}$ & $e_{7}$ \\
\hline$e_{0}$ & $e_{0}$ & $e_{1}$ & $e_{2}$ & $e_{3}$ & $e_{4}$ & $e_{5}$ & $e_{6}$ & $e_{7}$ \\
\hline$e_{1}$ & $e_{1}$ & $-e_{0}$ & $e_{3}$ & $-e_{2}$ & $e_{5}$ & $-e_{4}$ & $-e_{7}$ & $e_{6}$ \\
\hline$e_{2}$ & $e_{2}$ & $-e_{3}$ & $-e_{0}$ & $e_{1}$ & $e_{6}$ & $e_{7}$ & $-e_{4}$ & $-e_{5}$ \\
\hline$e_{3}$ & $e_{3}$ & $e_{2}$ & $-e_{1}$ & $-e_{0}$ & $e_{7}$ & $-e_{6}$ & $e_{5}$ & $-e_{4}$ \\
\hline$e_{4}$ & $e_{4}$ & $-e_{5}$ & $-e_{6}$ & $-e_{7}$ & $-e_{0}$ & $e_{1}$ & $e_{2}$ & $e_{3}$ \\
\hline$e_{5}$ & $e_{5}$ & $e_{4}$ & $-e_{7}$ & $e_{6}$ & $-e_{1}$ & $-e_{0}$ & $-e_{3}$ & $e_{2}$ \\
\hline$e_{6}$ & $e_{6}$ & $e_{7}$ & $e_{4}$ & $-e_{5}$ & $-e_{2}$ & $e_{3}$ & $-e_{0}$ & $-e_{1}$ \\
\hline$e_{7}$ & $e_{7}$ & $-e_{6}$ & $e_{5}$ & $e_{4}$ & $-e_{3}$ & $-e_{2}$ & $e_{1}$ & $-e_{0}$ \\
\hline
\end{tabular}
\caption{Multiplication table for the octonions in the form originally given by Cayley\cite{cayley1845xxviii}.}
\label{table:cayley-mult}
\end{center}
\end{table}

and we may achieve this form by the following assignment to STA elements: 

\be
e_0=1, \quad e_1=-I\sigma_1, \quad e_2=-I\sigma_2, \quad e_3=-I\sigma_3, \quad e_4=-I, \quad e_5=-\sigma_1, \quad e_6=-\sigma_2, \quad e_7=-\sigma_3
\ee

It may be wondered how assignments such as $e_5=-\sigma_1$ are going to work, since according to the multiplication table we want all the elements other than $e_0$ to have negative square, and of course $(-\sigma_1)^2=1$. This gives an opportunity to show how the product in (\ref{eqn:oct-prod}) works in an explicit case. If we put $\psi=\phi=\sigma_1$, and note $\phi_-=\sigma_1$ and $\phi_+=0$, then the product returns just

\be
\theta=\phirev_- \phi =\left(\tilde{\sig}_1\right) \sig_1 = -\sig_1 \sig_1 =-1
\label{eqn:sig1-sq}
\ee

as hoped. More generally we can see that `units' $e_i$, that commute with $\go$ will just be squared (in the STA sense), and units that anticommute with $\go$ will be multiplied by their reverse, and this pattern ensures a square in the octonion sense of $-1$ for each $i=1,\ldots,7$.  

It is good that we are able to reproduce the original multiplication laws as stated by Cayley, but this is just one table amongst a possible 480 variations all of which are compatible with the assignment $e_0=1$ (see e.g.\ the Wikipedia page \url{https://en.wikipedia.org/wiki/Octonion} for more details on this). A more recent choice of multiplication table to work from, is that given in the influential review of Octonions written in 2002 by John Baez\cite{baez2002octonions}. This table is well adapted to work with a popular way of expressing the rules of octonion multiplication, which is the {\em Fano plane}. In this, the octonion units are arranged at the vertices, midpoints and centre of an equilateral triangle, and the multiplication rules can be stated in terms of cyclic progression around the nodes.

The multiplication table given by Baez, which has also been used in the recent studies by Furey via the Fano plane version, is displayed in Table~\ref{table:baez-mult}.

\begin{table}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline & $e_{0}$ & $e_{1}$ & $e_{2}$ & $e_{3}$ & $e_{4}$ & $e_{5}$ & $e_{6}$ & $e_{7}$ \\
\hline$e_{0}$ & $e_{0}$ & $e_{1}$ & $e_{2}$ & $e_{3}$ & $e_{4}$ & $e_{5}$ & $e_{6}$ & $e_{7}$ \\
\hline$e_{1}$ & $e_{1}$ & $-e_{0}$ & $e_{4}$ & $e_{7}$ & $-e_{2}$ & $e_{6}$ & $-e_{5}$ & $-e_{3}$ \\
\hline$e_{2}$ & $e_{2}$ & $-e_{4}$ & $-e_{0}$ & $e_{5}$ & $e_{1}$ & $-e_{3}$ & $e_{7}$ & $-e_{6}$ \\
\hline$e_{3}$ & $e_{3}$ & $-e_{7}$ & $-e_{5}$ & $-e_{0}$ & $e_{6}$ & $e_{2}$ & $-e_{4}$ & $e_{1}$ \\
\hline$e_{4}$ & $e_{4}$ & $e_{2}$ & $-e_{1}$ & $-e_{6}$ & $-e_{0}$ & $e_{7}$ & $e_{3}$ & $-e_{5}$ \\
\hline$e_{5}$ & $e_{5}$ & $-e_{6}$ & $e_{3}$ & $-e_{2}$ & $-e_{7}$ & $-e_{0}$ & $e_{1}$ & $e_{4}$ \\
\hline$e_{6}$ & $e_{6}$ & $e_{5}$ & $-e_{7}$ & $e_{4}$ & $-e_{3}$ & $-e_{1}$ & $-e_{0}$ & $e_{2}$ \\
\hline$e_{7}$ & $e_{7}$ & $e_{3}$ & $e_{6}$ & $-e_{1}$ & $e_{5}$ & $-e_{4}$ & $-e_{2}$ & $-e_{0}$ \\ 
\hline
\end{tabular}
\caption{Multiplication table for the octonions as given in Baez\cite{baez2002octonions}.}
\label{table:baez-mult}
\end{center}
\end{table}

Additionally, in Fig.~\ref{fig:fano-plane},

\begin{figure}
\begin{center}
\begin{tikzpicture}[thick,scale=0.6, every node/.style={transform shape}]
\tikzstyle{point}=[ball color=cyan, circle, draw=black, inner sep=0.1cm, minimum size = 3cm]
\node (v7) at (0,0) [point] {\Huge $e_7$};

\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (150:4cm) arc [start angle=150, end angle=30, radius=4cm];
\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (30:4cm) arc [start angle=30, end angle=-90, radius=4cm];
\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (-90:4cm) arc [start angle=-90, end angle=-210, radius=4cm];
\node (v6) at (90:8cm) [point] {\Huge $e_6$};
\node (v3) at (210:8cm) [point] {\Huge $e_3$};
\node (v5) at (330:8cm) [point] {\Huge $e_5$};
\node (v4) at (150:4cm) [point] {\Huge $e_4$};
\node (v2) at (270:4cm) [point] {\Huge $e_2$};
\node (v1) at (30:4cm) [point] {\Huge $e_1$};
\begin{scope}[thick, every node/.style={sloped,allow upside down}]
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v3) -- (v4);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v4) -- (v6);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v6) -- (v1);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v1) -- (v5);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v5) -- (v2);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v2) -- (v3);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v5) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v4);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v6) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v2);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v3) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v1);
\end{scope}
\end{tikzpicture}
\caption{Fano plane for the multiplication table given in Table~\ref{table:baez-mult}. See text for a description of how the arrows relate to multiplication.}
\label{fig:fano-plane}
\end{center}
\end{figure}

we show the Fano plane construction as given by Baez\cite{baez2002octonions} and Furey\cite{Furey:2015tqa}.
This construction is a mnemonic to aid in applying the octonion multiplication rules, as given in Table~\ref{table:baez-mult}. Specifically, multiplying, in the direction indicated by the arrows, any two quantities joined by an arc or a line, should give the third element along that arc or line. To give two examples, we see by following along an arc that $e_4$ applied to the left of $e_1$ should give $e_2$ and, following along a line, $e_6$ applied to the left of $e_1$ should give $e_5$. Both of these agree with Table~\ref{table:baez-mult}.

Despite having settled on a multiplication table, we still need to make a choice of which STA elements represent which octonionic units, and we aim here to do this in such a way as the Fano plane diagram looks most symmetrical in terms of STA assignments. Given the central position of $e_7$ in the diagram, it is natural to equate this with either $I$ or $-I$, and then the sigma's and $I$sigma's fall naturally into symmetric positions around the triangle and the edge midpoints, as shown in Fig.~\ref{fig:fano-plane-with-STA}.

\begin{figure}
\begin{center}
\begin{tikzpicture}[thick,scale=0.6, every node/.style={transform shape}]
\tikzstyle{point}=[ball color=cyan, circle, draw=black, inner sep=0.1cm, minimum size = 3cm]
\node (v7) at (0,0) [point] {\Large$e_7=-I$};

\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (150:4cm) arc [start angle=150, end angle=30, radius=4cm];
\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (30:4cm) arc [start angle=30, end angle=-90, radius=4cm];
\draw[thick,decoration={markings, mark=at position 0.7 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (-90:4cm) arc [start angle=-90, end angle=-210, radius=4cm];
\node (v6) at (90:8cm) [point] {\Large $e_6=\sigma_2$};
\node (v3) at (210:8cm) [point] {\Large $e_3=\sigma_1$};
\node (v5) at (330:8cm) [point] {\Large $e_5=\sigma_3$};
\node (v4) at (150:4cm) [point] {\Large$e_4=-I\sigma_3$};
\node (v2) at (270:4cm) [point] {\Large $e_2=-I\sigma_2$};
\node (v1) at (30:4cm) [point] {\Large $e_1=-I\sigma_1$};
\begin{scope}[thick, every node/.style={sloped,allow upside down}]
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v3) -- (v4);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v4) -- (v6);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v6) -- (v1);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v1) -- (v5);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v5) -- (v2);
\draw[thick,decoration={markings, mark=at position 0.5 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v2) -- (v3);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v5) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v4);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v6) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v2);
\draw[thick,decoration={markings, mark=at position 0.75 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v3) -- (v7);
\draw[thick,decoration={markings, mark=at position 0.8 with {\arrow[scale=3]{stealth}}},postaction={decorate}] (v7) -- (v1);
\end{scope}
\end{tikzpicture}
\caption{The same as in Fig.~\ref{fig:fano-plane} but now with the STA assignments to each node indicated.}
\label{fig:fano-plane-with-STA}
\end{center}
\end{figure}

The resulting allocations, which we will box to indicate this is the final form we will use, are

\be
\boxed{
e_0=1, \quad e_1=-I\sigma_1, \quad e_2=-I\sigma_2, \quad e_3=\sigma_1, \quad e_4=-I\sigma_3, \quad e_5=\sigma_3, \quad e_6=\sigma_2, \quad e_7=-I
}
\label{eqn:final-STA-allocs}
\ee


We need to stress that in this diagram (Fig.~\ref{fig:fano-plane-with-STA}) the implied multiplications are {\em octonionic} multiplications as given by (\ref{eqn:oct-prod}), and therefore composed (in general) of the sum of up to 4 GA multiplications along with possible reversions. Thus there is no implication that the ordinary GA product follows the same cyclic rules as the octonion ones in this figure, though if the reader tries it, they will find that the products are correct up to signs. E.g.\ $e_6 e_1$ is equal to $e_5$ in octonion terms, meaning that $\sig_2 \star (-I\sig_1)=\sig_3$, but the GA product $\sig_2 (-I\sig_1)$ is minus rather than plus $\sig_3$.

There is more that can be said about these basic aspects of the representation of octonions within the STA, and some further examples of calculations with STA elements, based upon our main equations 
(\ref{eqn:oct-prod}), (\ref{eqn:conj-def}), (\ref{eqn:norm-res}) and
(\ref{eqn:final-STA-allocs}), can be found in the paper also in these proceedings by Eckhard Hitzer\cite{eckhard-oct}, who then goes on to consider the embedding of octonions into some different Clifford algebras, not just the STA.
