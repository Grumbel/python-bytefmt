;; bytefmt - Convert a byte count into a human readable string
;; Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

(use-modules (guix packages)
             (guix gexp)
             (guix git-download)
             (guix build-system python)
             (guix licenses)
             (gnu packages freedesktop)
             (gnu packages python))

(define %source-dir (dirname (current-filename)))

(define-public bytefmt
  (package
    (name "bytefmt")
    (version "0.1.1")
    (source
     (local-file %source-dir
                 #:recursive? #t
                 #:select? (git-predicate %source-dir)))
    (build-system python-build-system)
    (inputs
     `(("python" ,python)))
    (home-page "https://gitlab.com/grumbel/python-bytefmt")
    (synopsis "Convert bytes to human readable format and back")
    (description "Simple Python library to format bytes into a human
readable format and parse a human readable format back into bytes.")
    (license gpl3+)))

bytefmt

;; EOF ;;
