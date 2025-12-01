using BibliotecaOnline.Data;
using Microsoft.AspNetCore.Mvc;
using System.Linq;

namespace BibliotecaOnline.Controllers
{
    public class AccountController : Controller
    {
        private readonly ApplicationDbContext _context;

        public AccountController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Login(string nombreUsuario, string email, string password)
        {
            var usuario = _context.Usuarios
                .FirstOrDefault(u => u.Email == email && u.Password == password);

            if (usuario == null)
            {
                ViewBag.Error = "Credenciales incorrectas.";
                ViewBag.NombreUsuario = nombreUsuario;
                ViewBag.Email = email;
                return View();
            }

            HttpContext.Session.SetString("Usuario", usuario.NombreUsuario);

            return RedirectToAction("Index", "Libros");
        }

        public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Login");
        }
    }
}
