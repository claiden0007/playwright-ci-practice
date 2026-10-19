from playwright.sync_api import Page, expect

def test_login_form(page: Page):
    page.set_content("""
        <html>
            <body>
                <input id="username" placeholder="Username">
                <input id="password" type="password"
                       placeholder="Password">
                <button id="login">Login</button>
                <p id="message" style="display: none;">
                    Login successful!
                </p>

                <script>
                    document.getElementById("login")
                        .addEventListener("click", () => {
                            document.getElementById("message")
                                .style.display = "block";
                        });
                </script>
            </body>
        </html>
    """)

    page.locator("#username").fill("Claiden")
    page.locator("#password").fill("Test123")
    page.locator("#login").click()

    expect(page.locator("#message")).to_have_text("Login successful!")
