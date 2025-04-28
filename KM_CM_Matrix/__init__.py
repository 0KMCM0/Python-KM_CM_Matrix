"""
https://github.com/0KMCM0/Python-KM_CM_Matrix
"""

from typing import TypeVar as _TypeVar, Generic as _Generic, Any as _Any

_T = _TypeVar( '_T' )

class Matrix( _Generic[ _T ] ):
    def __init__( self, Axes: list[ list[ _T ] ] ) -> None:
        self.m_lAxes: list[ list[ _T ] ] = Axes

    def __iter__( self ):
        X, Y = -1, -1
        for A in self.m_lAxes:
            Y += 1
            for E in A:
                X += 1
                yield X, Y, E

    def __str__( self ) -> str:
        S = '[ ' #'Matrix[ '
        I = ' ' * len( S )
        PX, PY = -1, -1
        for X in self.m_lAxes:
            PY += 1
            R = []
            for Y in X:
                PX += 1
                R.append( f'{ PX }:{ PY }:{ repr( Y ) }' )
            S += f'[ { ', '.join( R ) } ]\n{ I }'
        return S.rstrip() + ' ]'
    def __repr__( self ) -> str:
        return f'Matrix({ ','.join( [ f'[{ ','.join( [ repr( Y ) for Y in X ] ) }]' for X in self.m_lAxes ] ) })'

    def __abs__( self ): return Matrix( [ [ abs( Y ) for Y in X ] for X in self.m_lAxes ] )
    def __neg__( self ): return Matrix( [ [ -Y for Y in X ] for X in self.m_lAxes ] )

    def __setitem__( self, Index: tuple[ int, int ], Value: _T ) -> None:
        self.m_lAxes[ Index[ 1 ] ][ Index[ 0 ] ] = Value
    def __getitem__( self, Index: tuple[ int, int ] ) -> _T:
        return self.m_lAxes[ Index[ 1 ] ][ Index[ 0 ] ]

    def __contains__( self, Item: _Any ) -> bool:
        for X in self.m_lAxes:
            for Y in X:
                try:
                    if Y == Item: return True
                except: pass
        return False

    def __eq__( self, Other: 'Matrix' ) -> bool:
        for A, B in zip( self.m_lAxes, Other.m_lAxes ):
            if A != B: return False
        return True
    def __ne__( self, Other: 'Matrix' ) -> bool:
        for A, B in zip( self.m_lAxes, Other.m_lAxes ):
            if A == B: return False
        return True

    def __Operator__( self, Other, Func ) -> 'Matrix[ _T ]':
        if isinstance( Other, Matrix ):
            M = []
            for X, Y in zip( self.m_lAxes, Other.m_lAxes ):
                L = []
                for I in range( 0, len( X ) ):
                    L.append( Func( X[ I ], Y[ I ] ) )
                M.append( L )
            return Matrix( M )
        return Matrix( [ [ Func( Y, Other ) for Y in X ] for X in self.m_lAxes ] )

    def __ROperator__( self, Other, Func ) -> 'Matrix[ _T ]':
        if isinstance( Other, Matrix ):
            M = []
            for X, Y in zip( self.m_lAxes, Other.m_lAxes ):
                L = []
                for I in range( 0, len( X ) ):
                    L.append( Func( Y[ I ], X[ I ] ) )
                M.append( L )
            return Matrix( M )
        return Matrix( [ [ Func( Other, Y ) for Y in X ] for X in self.m_lAxes ] )

    def __add__( self, Other ) -> 'Matrix[ _T ]': return      self.__Operator__( Other, lambda A, B: A + B )
    def __sub__( self, Other ) -> 'Matrix[ _T ]': return      self.__Operator__( Other, lambda A, B: A - B )
    def __mul__( self, Other ) -> 'Matrix[ _T ]': return      self.__Operator__( Other, lambda A, B: A * B )
    def __pow__( self, Other ) -> 'Matrix[ _T ]': return      self.__Operator__( Other, lambda A, B: A ** B )
    def __mod__( self, Other ) -> 'Matrix[ _T ]': return      self.__Operator__( Other, lambda A, B: A % B )
    def __truediv__( self, Other ) -> 'Matrix[ _T ]': return  self.__Operator__( Other, lambda A, B: A / B )
    def __floordiv__( self, Other ) -> 'Matrix[ _T ]': return self.__Operator__( Other, lambda A, B: A // B )

    def __radd__( self, Other ) -> 'Matrix[ _T ]': return      self.__ROperator__( Other, lambda A, B: A + B )
    def __rsub__( self, Other ) -> 'Matrix[ _T ]': return      self.__ROperator__( Other, lambda A, B: A - B )
    def __rmul__( self, Other ) -> 'Matrix[ _T ]': return      self.__ROperator__( Other, lambda A, B: A * B )
    def __rpow__( self, Other ) -> 'Matrix[ _T ]': return      self.__ROperator__( Other, lambda A, B: A ** B )
    def __rmod__( self, Other ) -> 'Matrix[ _T ]': return      self.__ROperator__( Other, lambda A, B: A % B )
    def __rtruediv__( self, Other ) -> 'Matrix[ _T ]': return  self.__ROperator__( Other, lambda A, B: A / B )
    def __rfloordiv__( self, Other ) -> 'Matrix[ _T ]': return self.__ROperator__( Other, lambda A, B: A // B )
