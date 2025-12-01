using BibliotecaOnline.Data;
using BibliotecaOnline.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BibliotecaOnline.Controllers
{
    public class LibrosController : Controller
    {
        private readonly ApplicationDbContext _context;

        public LibrosController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            return View(_context.Libros.ToList());
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Libro libro)
        {
            if (ModelState.IsValid)
            {
                _context.Libros.Add(libro);
                _context.SaveChanges();
                TempData["Success"] = "Libro creado correctamente.";
                return RedirectToAction("Index");
            }

            return View(libro);
        }

        public IActionResult Edit(int id)
        {
            var libro = _context.Libros.Find(id);
            if (libro == null) return NotFound();

            return View(libro);
        }

        [HttpPost]
        public IActionResult Edit(Libro libro)
        {
            if (ModelState.IsValid)
            {
                _context.Libros.Update(libro);
                _context.SaveChanges();
                TempData["Success"] = "Libro actualizado correctamente.";
                return RedirectToAction("Index");
            }

            return View(libro);
        }

        public IActionResult Delete(int id)
        {
            var libro = _context.Libros.Find(id);
            if (libro == null) return NotFound();

            return View(libro);
        }

        [HttpPost, ActionName("Delete")]
        public IActionResult DeleteConfirmed(int id)
        {
            var libro = _context.Libros.Find(id);
            _context.Libros.Remove(libro);
            _context.SaveChanges();
            TempData["Success"] = "Libro eliminado correctamente.";
            return RedirectToAction("Index");
        }

        public IActionResult Details(int id)
        {
            var libro = _context.Libros.Find(id);
            if (libro == null) return NotFound();

            return View(libro);
        }
    }
}
