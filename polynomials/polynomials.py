from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self,other):
        if isinstance(other, Polynomial):
            common = min(self.degree(),other.degree())+1
            coefs = tuple(a-b for a,b in zip(self.coefficients,other.coefficients))
           
            coefs += self.coefficients[common:] + tuple([-1*i for i in other.coefficients[common:]])
            return Polynomial(coefs)
    
        elif isinstance(other,Number):
            return Polynomial((self.coefficients[0] - other,) + (self.coefficients[1:]))
    def __rsub__(self,other):
        x = self-other
        return Polynomial(tuple([-1*i for i in x.coefficients]))
    
    def __mul__(self,other):
        if isinstance(other,Number):
            coefs = tuple(other*i for i in self.coefficients)
            return Polynomial(coefs)
        elif isinstance(other,Polynomial):
            len_self, len_other = len(self.coefficients),len(other.coefficients)
            coefs_ls = [0] * (len_other+len_self-1)
            for i,coeff_1 in enumerate(self.coefficients):
                for j,coeff_2 in enumerate(other.coefficients):
                    coefs_ls[i+j] += coeff_1 * coeff_2
            
            coefs = tuple(coefs_ls)
            return Polynomial(coefs)
    
    def __rmul__(self,other):
        return self*other
    
    def __pow__(self,pow):
        if pow == 0: return Polynomial((1,))
        elif pow == 1: return self
        res = self
        for i in range(pow-1):
            res = res * self
        return res
    
    def __call__(self,x):
        sm = 0
        ln = len(self.coefficients) - 1
        if x == 0: return self.coefficients[0]
        elif x == 1: return sum(self.coefficients)
        else:
            for i, coeff_1 in enumerate(self.coefficients):
                sm += coeff_1 * (x**i)
        return sm
