import 'package:flutter/material.dart';
import 'package:my_app/widgets/bg_image.dart';
import 'package:my_app/utils/Constants.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  String uName = "anil";
  String pwd = "anil";
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
                                controller: userNameController,
                                decoration: InputDecoration(
                                    hintText: "Enter User Name",
                                    labelText: "UserName"),
                              ),
                              SizedBox(
                                height: 20,
                              ),
                              TextFormField(
                                controller: passwordController,
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
                            if (userNameController.text == uName &&
                                passwordController.text == pwd) {
                              c.storeLoggedInStatus(true);
                              Navigator.pushReplacementNamed(context, "/home");
                            } else {
                              //Text("Invalid Username & Password");
                            }
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
