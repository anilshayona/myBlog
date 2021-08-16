import 'package:flutter/material.dart';
import 'package:my_app/bg_image.dart';
import 'package:my_app/utils/Constants.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final userNameController = TextEditingController();
  final passwordController = TextEditingController();
  Constants c = new Constants();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Login Page"),
        ),
        body: Stack(
          fit: StackFit.expand,
          children: [
            BgImage(),
            Center(
              child: Padding(
                padding: const EdgeInsets.all(10.0),
                child: SingleChildScrollView(
                  child: Card(
                    child: Column(
                      children: [
                        Form(
                            child: Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: Column(
                            children: [
                              TextFormField(
                                decoration: InputDecoration(
                                    hintText: "Enter User Name",
                                    labelText: "UserName"),
                              ),
                              SizedBox(
                                height: 20,
                              ),
                              TextFormField(
                                obscureText: true,
                                decoration: InputDecoration(
                                    hintText: "Enter Password",
                                    labelText: "Password"),
                              ),
                            ],
                          ),
                        )),
                        SizedBox(
                          height: 20,
                        ),
                        ElevatedButton(
                          onPressed: () async {
                            c.storeLoggedInStatus(true);
                            Navigator.pushReplacementNamed(context, "/home");
                          },
                          child: Text("Sign In"),
                        )
                      ],
                    ),
                  ),
                ),
              ),
            )
          ],
        ));
  }
}
