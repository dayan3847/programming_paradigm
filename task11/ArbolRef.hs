{- Estructura del árbol -}
data Abb a = End | Node a (Abb a) (Abb a) deriving (Show)

-- Devuelve True o False si el nodo se halla en el árbol
-- BuscarNodo (Valor a buscar) (Árbol)
findNode :: (Ord a) => a -> Abb a -> Bool
findNode nodeToFind End = False
findNode nodeToFind (Node a izq der)
 | nodeToFind == a = True
 | nodeToFind < a = findNode nodeToFind izq
 | otherwise = findNode nodeToFind der


--let an = Node 104 (Node 71 (Node 17 (Node 3 End End) (Node 18 End End)) (Node 19 End End)) (Node 240 (Node 108 End (Node 110 End End)) (Node 245 End End))
--let at = Node "a" (node "b" End End)(Node "c" End End)