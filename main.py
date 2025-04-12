import { useEffect, useState } from "react"; import { Input } from "@/components/ui/input"; import { Button } from "@/components/ui/button"; import { Card, CardContent } from "@/components/ui/card";

export default function Essenzia() { const [query, setQuery] = useState(""); const [perfumes, setPerfumes] = useState([]); const [cart, setCart] = useState([]); const [isAuthenticated, setIsAuthenticated] = useState(false); const [username, setUsername] = useState(""); const [password, setPassword] = useState("");

useEffect(() => { if (isAuthenticated) { fetch("http://localhost:4000/perfumes") .then(res => res.json()) .then(data => setPerfumes(data));

fetch("http://localhost:4000/cart")
    .then(res => res.json())
    .then(data => setCart(data.items || []));
}

}, [isAuthenticated]);

const addToCart = async (perfume) => { const res = await fetch("http://localhost:4000/cart", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ item: perfume }) }); const data = await res.json(); setCart(data.items); };

const filtered = perfumes.filter(p => p.name.toLowerCase().includes(query.toLowerCase()) );

const handleLogin = () => { if (username === "admin" && password === "essenzia2025") { setIsAuthenticated(true); } else { alert("Usuario o contraseña incorrectos."); } };

if (!isAuthenticated) { return ( <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4"> <h1 className="text-3xl font-bold mb-6">Acceso a Essenzia</h1> <div className="space-y-4 w-full max-w-xs"> <Input placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} /> <Input placeholder="Contraseña" type="password" value={password} onChange={(e) => setPassword(e.target.value)} /> <Button onClick={handleLogin} className="w-full">Entrar</Button> </div> </div> ); }

return ( <div className="min-h-screen bg-white text-gray-900 p-4"> <header className="text-center mb-8"> <h1 className="text-4xl font-bold tracking-wide">Essenzia</h1> <p className="text-sm text-gray-500">Perfumes de marca. Belleza auténtica.</p> </header>

<div className="max-w-xl mx-auto mb-6">
    <Input
      placeholder="Buscar perfume..."
      value={query}
      onChange={(e) => setQuery(e.target.value)}
    />
  </div>

  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 max-w-5xl mx-auto">
    {filtered.map((perfume) => (
      <Card key={perfume._id} className="rounded-2xl shadow p-4">
        <CardContent>
          <h2 className="text-lg font-semibold mb-2">{perfume.name}</h2>
          <p className="mb-2">{perfume.price}</p>
          <Button onClick={() => addToCart(perfume)}>Agregar a la cesta</Button>
        </CardContent>
      </Card>
    ))}
  </div>

  <div className="max-w-2xl mx-auto mt-10 p-4 border-t">
    <h2 className="text-2xl font-semibold mb-4">Cesta</h2>
    {cart.length === 0 ? (
      <p className="text-gray-500">Tu cesta está vacía.</p>
    ) : (
      <ul className="space-y-2">
        {cart.map((item, index) => (
          <li key={index} className="flex justify-between">
            <span>{item.name}</span>
            <span>{item.price}</span>
          </li>
        ))}
      </ul>
    )}
  </div>

  <footer className="text-center mt-16 text-sm text-gray-400 border-t pt-4">
    <p>Contacto: contacto@essenzia.com</p>
    <p>&copy; 2025 Essenzia. Todos los derechos reservados.</p>
  </footer>
</div>

); }

