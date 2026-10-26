import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np


class PageRankApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PageRank - Linear Algebra Application")
        self.root.geometry("1200x750")

        self.links = []
        self.page_entries = []

        self.create_input_screen()

    # ============================================================
    # INPUT SCREEN
    # ============================================================

    def create_input_screen(self):

        title = tk.Label(
            self.root,
            text="WEBPAGE RANKING USING LINEAR ALGEBRA",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="Google PageRank using Matrices, Eigenvalues and Eigenvectors",
            font=("Arial", 11)
        )
        subtitle.pack()

        # --------------------------------------------------------
        # 1. WEBPAGE SETUP
        # --------------------------------------------------------

        setup_frame = tk.LabelFrame(
            self.root,
            text="1. Webpage Setup",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )

        setup_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        tk.Label(
            setup_frame,
            text="Number of Webpages:"
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        self.num_pages_entry = tk.Entry(
            setup_frame,
            width=10
        )

        self.num_pages_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        self.num_pages_entry.insert(
            0,
            "3"
        )

        tk.Button(
            setup_frame,
            text="Create Pages",
            command=self.create_pages,
            width=15
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        # --------------------------------------------------------
        # 2. PAGE NAMES
        # --------------------------------------------------------

        self.pages_frame = tk.LabelFrame(
            self.root,
            text="2. Page Names",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )

        self.pages_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # --------------------------------------------------------
        # 3. WEBPAGE LINKS
        # --------------------------------------------------------

        self.links_frame = tk.LabelFrame(
            self.root,
            text="3. Webpage Links",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )

        self.links_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        tk.Label(
            self.links_frame,
            text="From:"
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        self.from_combo = ttk.Combobox(
            self.links_frame,
            state="readonly",
            width=20
        )

        self.from_combo.grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Label(
            self.links_frame,
            text="To:"
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.to_combo = ttk.Combobox(
            self.links_frame,
            state="readonly",
            width=20
        )

        self.to_combo.grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            self.links_frame,
            text="ADD LINK",
            command=self.add_link,
            width=12
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        tk.Button(
            self.links_frame,
            text="CLEAR LINKS",
            command=self.clear_links,
            width=12
        ).grid(
            row=0,
            column=5,
            padx=10
        )

        self.links_listbox = tk.Listbox(
            self.links_frame,
            width=70,
            height=6
        )

        self.links_listbox.grid(
            row=1,
            column=0,
            columnspan=6,
            pady=10
        )

        # --------------------------------------------------------
        # 4. PAGERANK PARAMETERS
        # --------------------------------------------------------

        parameter_frame = tk.LabelFrame(
            self.root,
            text="4. PageRank Parameters",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )

        parameter_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        tk.Label(
            parameter_frame,
            text="Damping Factor:"
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        self.damping_entry = tk.Entry(
            parameter_frame,
            width=10
        )

        self.damping_entry.grid(
            row=0,
            column=1
        )

        self.damping_entry.insert(
            0,
            "0.85"
        )

        tk.Label(
            parameter_frame,
            text="Tolerance:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.tolerance_entry = tk.Entry(
            parameter_frame,
            width=12
        )

        self.tolerance_entry.grid(
            row=0,
            column=3
        )

        self.tolerance_entry.insert(
            0,
            "0.000001"
        )

        # --------------------------------------------------------
        # RUN BUTTON
        # --------------------------------------------------------

        tk.Button(
            self.root,
            text="RUN COMPLETE ANALYSIS",
            command=self.run_analysis,
            font=("Arial", 14, "bold"),
            width=30,
            height=2
        ).pack(
            pady=20
        )

    # ============================================================
    # CREATE PAGES
    # ============================================================

    def create_pages(self):

        try:
            n = int(
                self.num_pages_entry.get()
            )

            if n < 2 or n > 10:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter a number between 2 and 10."
            )
            return

        for widget in self.pages_frame.winfo_children():
            widget.destroy()

        self.page_entries = []

        for i in range(n):

            tk.Label(
                self.pages_frame,
                text=f"Page {i + 1}:"
            ).grid(
                row=i // 3,
                column=(i % 3) * 2,
                padx=5,
                pady=5
            )

            entry = tk.Entry(
                self.pages_frame,
                width=20
            )

            entry.grid(
                row=i // 3,
                column=(i % 3) * 2 + 1,
                padx=5,
                pady=5
            )

            entry.insert(
                0,
                f"Page {i + 1}"
            )

            entry.bind(
                "<KeyRelease>",
                lambda event: self.update_dropdowns()
            )

            self.page_entries.append(
                entry
            )

        self.links = []

        self.links_listbox.delete(
            0,
            tk.END
        )

        self.update_dropdowns()

    # ============================================================
    # UPDATE DROPDOWNS
    # ============================================================

    def update_dropdowns(self):

        if not self.page_entries:
            return

        pages = [
            entry.get().strip()
            for entry in self.page_entries
        ]

        dropdown_pages = []

        for i, page in enumerate(pages):

            if page:
                dropdown_pages.append(
                    page
                )
            else:
                dropdown_pages.append(
                    f"Page {i + 1}"
                )

        self.from_combo["values"] = dropdown_pages
        self.to_combo["values"] = dropdown_pages

        if dropdown_pages:

            if self.from_combo.get() not in dropdown_pages:
                self.from_combo.current(0)

            if self.to_combo.get() not in dropdown_pages:
                self.to_combo.current(0)

    # ============================================================
    # ADD LINK
    # ============================================================

    def add_link(self):

        source = self.from_combo.get()
        destination = self.to_combo.get()

        if not source or not destination:
            messagebox.showwarning(
                "Warning",
                "Select both webpages."
            )
            return

        if source == destination:
            messagebox.showwarning(
                "Warning",
                "A webpage cannot link to itself."
            )
            return

        link = (
            source,
            destination
        )

        if link in self.links:
            messagebox.showwarning(
                "Warning",
                "This link already exists."
            )
            return

        self.links.append(
            link
        )

        self.links_listbox.insert(
            tk.END,
            f"{source}  →  {destination}"
        )

    # ============================================================
    # CLEAR LINKS
    # ============================================================

    def clear_links(self):

        self.links = []

        self.links_listbox.delete(
            0,
            tk.END
        )

    # ============================================================
    # BUILD ADJACENCY MATRIX
    #
    # ROWS    = DESTINATION
    # COLUMNS = SOURCE
    #
    # A[i][j] = 1
    # means page j links to page i
    # ============================================================

    def build_adjacency_matrix(self):

        pages = [
            entry.get().strip()
            for entry in self.page_entries
        ]

        if any(
            not page
            for page in pages
        ):
            raise ValueError(
                "Every webpage must have a name."
            )

        if len(set(pages)) != len(pages):
            raise ValueError(
                "Webpage names must be unique."
            )

        n = len(pages)

        A = np.zeros(
            (n, n)
        )

        page_index = {
            page: i
            for i, page in enumerate(pages)
        }

        for source, destination in self.links:

            source_index = page_index[source]
            destination_index = page_index[destination]

            # ROW = DESTINATION
            # COLUMN = SOURCE

            A[
                destination_index,
                source_index
            ] = 1

        return pages, A

    # ============================================================
    # BUILD TRANSITION MATRIX
    #
    # Each column represents where the rank of a source page
    # is distributed.
    # ============================================================

    def build_transition_matrix(
        self,
        A
    ):

        n = A.shape[0]

        M = np.zeros(
            (n, n)
        )

        for source in range(n):

            outgoing_links = np.sum(
                A[:, source]
            )

            if outgoing_links == 0:

                M[:, source] = 1 / n

            else:

                M[:, source] = (
                    A[:, source]
                    /
                    outgoing_links
                )

        return M

    # ============================================================
    # BUILD GOOGLE MATRIX
    #
    # G = dM + (1-d)(1/N)J
    # ============================================================

    def build_google_matrix(
        self,
        M,
        damping
    ):

        n = M.shape[0]

        J = np.ones(
            (n, n)
        )

        G = (
            damping * M
            +
            (1 - damping) / n * J
        )

        return G

    # ============================================================
    # PAGERANK ITERATION
    # ============================================================

    def calculate_pagerank(
        self,
        G,
        tolerance
    ):

        n = G.shape[0]

        # Initial PageRank
        rank = np.ones(
            (n, 1)
        ) / n

        iterations = []

        iterations.append(
            rank.copy()
        )

        for _ in range(1000):

            new_rank = G @ rank

            iterations.append(
                new_rank.copy()
            )

            difference = np.linalg.norm(
                new_rank - rank
            )

            rank = new_rank

            if difference < tolerance:
                break

        return rank, iterations

    # ============================================================
    # RUN ANALYSIS
    # ============================================================

    def run_analysis(self):

        if not self.page_entries:

            messagebox.showerror(
                "Error",
                "Create the webpages first."
            )

            return

        try:

            pages, A = (
                self.build_adjacency_matrix()
            )

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            return

        if not self.links:

            messagebox.showerror(
                "Error",
                "Add at least one webpage link."
            )

            return

        try:

            damping = float(
                self.damping_entry.get()
            )

            tolerance = float(
                self.tolerance_entry.get()
            )

            if not 0 < damping < 1:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid damping factor and tolerance."
            )

            return

        M = self.build_transition_matrix(
            A
        )

        G = self.build_google_matrix(
            M,
            damping
        )

        rank, iterations = (
            self.calculate_pagerank(
                G,
                tolerance
            )
        )

        self.show_results(
            pages,
            A,
            M,
            G,
            rank,
            iterations,
            damping,
            tolerance
        )

    # ============================================================
    # RESULTS WINDOW
    # ============================================================

    def show_results(
        self,
        pages,
        A,
        M,
        G,
        rank,
        iterations,
        damping,
        tolerance
    ):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "PageRank Analysis Results"
        )

        window.geometry(
            "1100x750"
        )

        notebook = ttk.Notebook(
            window
        )

        notebook.pack(
            fill="both",
            expand=True
        )

        # --------------------------------------------------------
        # TAB 1 - MATRIX REPRESENTATION
        # --------------------------------------------------------

        frame1 = tk.Frame(
            notebook
        )

        notebook.add(
            frame1,
            text="1. Matrix Representation"
        )

        self.add_matrix(
            frame1,
            "ADJACENCY MATRIX\n\n"
            "Rows = Destination\n"
            "Columns = Source\n\n"
            "A[i,j] = 1 means webpage j links to webpage i.",
            A,
            pages
        )

        # --------------------------------------------------------
        # TAB 2 - GOOGLE MATRIX
        # --------------------------------------------------------

        frame2 = tk.Frame(
            notebook
        )

        notebook.add(
            frame2,
            text="2. Google Matrix"
        )

        tk.Label(
            frame2,
            text=(
                "TRANSITION MATRIX M\n\n"
                "Each column distributes the rank of a source webpage."
            ),
            font=("Arial", 12, "bold")
        ).pack(
            pady=10
        )

        self.add_matrix(
            frame2,
            "",
            M,
            pages
        )

        formula = tk.Label(
            frame2,
            text=(
                f"\nGoogle Matrix:\n\n"
                f"G = dM + (1-d)(1/N)J\n\n"
                f"d = {damping}\n"
                f"N = {len(pages)}"
            ),
            font=("Arial", 12)
        )

        formula.pack(
            pady=10
        )

        self.add_matrix(
            frame2,
            "GOOGLE MATRIX G",
            G,
            pages
        )

        # --------------------------------------------------------
        # TAB 3 - PAGERANK ITERATIONS
        # --------------------------------------------------------

        frame3 = tk.Frame(
            notebook
        )

        notebook.add(
            frame3,
            text="3. PageRank Iterations"
        )

        canvas = tk.Canvas(
            frame3
        )

        scrollbar = ttk.Scrollbar(
            frame3,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tk.Frame(
            canvas
        )

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=scroll_frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        for i, vector in enumerate(
            iterations
        ):

            if i == 0:

                title = (
                    "Initial PageRank Matrix r₀"
                )

            else:

                title = (
                    f"Iteration {i}: r{i} = G r{i-1}"
                )

            self.add_matrix(
                scroll_frame,
                title,
                vector,
                pages,
                compact=True
            )

        # --------------------------------------------------------
        # TAB 4 - EIGENVALUE & FINAL RANKING
        # --------------------------------------------------------

        frame4 = tk.Frame(
            notebook
        )

        notebook.add(
            frame4,
            text="4. Eigenvalue & Final Ranking"
        )

        # Calculate eigenvalues of G
        eigenvalues, eigenvectors = np.linalg.eig(
            G
        )

        # Find eigenvalue closest to 1
        eigenvalue_index = np.argmin(
            np.abs(
                eigenvalues - 1
            )
        )

        dominant_eigenvalue = (
            eigenvalues[
                eigenvalue_index
            ]
        )

        # G*r
        Gr = G @ rank

        tk.Label(
            frame4,
            text=(
                "EIGENVALUE / EIGENVECTOR CONNECTION"
            ),
            font=("Arial", 14, "bold")
        ).pack(
            pady=10
        )

        tk.Label(
            frame4,
            text=(
                "At convergence:\n\n"
                "G r = r\n\n"
                "Therefore:\n\n"
                "G r = 1 r\n\n"
                "Comparing with A v = λ v:\n\n"
                "Eigenvalue λ = 1\n"
                "Eigenvector = PageRank vector r"
            ),
            font=("Arial", 12)
        ).pack(
            pady=5
        )

        self.add_matrix(
            frame4,
            "FINAL PAGERANK VECTOR r",
            rank,
            pages,
            compact=True
        )

        self.add_matrix(
            frame4,
            "G r",
            Gr,
            pages,
            compact=True
        )

        tk.Label(
            frame4,
            text=(
                f"Eigenvalue closest to 1 = "
                f"{dominant_eigenvalue.real:.6f}\n\n"
                "Since G r ≈ r, the PageRank vector "
                "is the eigenvector corresponding to λ = 1."
            ),
            font=("Arial", 11)
        ).pack(
            pady=10
        )

        # --------------------------------------------------------
        # FINAL RANKING
        # --------------------------------------------------------

        ranking = []

        for i in range(
            len(pages)
        ):

            ranking.append(
                (
                    pages[i],
                    float(
                        rank[i, 0]
                    )
                )
            )

        ranking.sort(
            key=lambda x: x[1],
            reverse=True
        )

        ranking_frame = tk.LabelFrame(
            frame4,
            text="Final Webpage Ranking",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10
        )

        ranking_frame.pack(
            pady=10
        )

        for position, (
            page,
            score
        ) in enumerate(
            ranking,
            start=1
        ):

            tk.Label(
                ranking_frame,
                text=(
                    f"{position}.  "
                    f"{page}    "
                    f"{score:.6f}"
                ),
                font=("Arial", 12)
            ).pack(
                anchor="w",
                padx=10,
                pady=2
            )

    # ============================================================
    # DISPLAY MATRIX AS A TABLE
    # ============================================================

    def add_matrix(
        self,
        parent,
        title,
        matrix,
        labels,
        compact=False
    ):

        if title:

            tk.Label(
                parent,
                text=title,
                font=("Arial", 12, "bold")
            ).pack(
                pady=8
            )

        matrix_frame = tk.Frame(
            parent
        )

        matrix_frame.pack(
            pady=5
        )

        matrix = np.asarray(
            matrix
        )

        rows, columns = matrix.shape

        # Empty corner
        tk.Label(
            matrix_frame,
            text=""
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=5
        )

        # Column labels = SOURCE
        for j in range(columns):

            tk.Label(
                matrix_frame,
                text=labels[j],
                font=("Arial", 11, "bold"),
                width=12,
                relief="ridge",
                borderwidth=1
            ).grid(
                row=0,
                column=j + 1,
                padx=1,
                pady=1
            )

        # Rows = DESTINATION
        for i in range(rows):

            tk.Label(
                matrix_frame,
                text=labels[i],
                font=("Arial", 11, "bold"),
                width=12,
                relief="ridge",
                borderwidth=1
            ).grid(
                row=i + 1,
                column=0,
                padx=1,
                pady=1
            )

            for j in range(columns):

                value = matrix[i, j]

                if abs(value) < 0.0000005:
                    value = 0

                tk.Label(
                    matrix_frame,
                    text=f"{value:.6f}",
                    font=("Consolas", 11),
                    width=12,
                    relief="ridge",
                    borderwidth=1
                ).grid(
                    row=i + 1,
                    column=j + 1,
                    padx=1,
                    pady=1
                )


# ================================================================
# MAIN
# ================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = PageRankApp(
        root
    )

    root.mainloop()