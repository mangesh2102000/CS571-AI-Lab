himalayan(a).
himalayan(b).
himalayan(c).
himalayan(X):-mountain(X);ski(X).

like(a, rain).
like(a, snow).
notlike(b, Y):-like(a, Y).
notlike(a, V):-like(b, V).

mountain(Z):-notlike(Z, rain).

ski(W):-like(W,snow).

g(M):-himalayan(M),mountain(M),not(ski(M)),!.