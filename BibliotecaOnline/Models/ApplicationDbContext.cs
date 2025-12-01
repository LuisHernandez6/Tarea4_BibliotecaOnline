using BibliotecaOnline.Models;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace BibliotecaOnline.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Usuario> Usuarios { get; set; }
        public DbSet<Libro> Libros { get; set; }
    }
}
